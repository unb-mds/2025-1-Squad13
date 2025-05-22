import psycopg2
from sqlalchemy import create_engine, text, String, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import Session, mapped_column, relationship
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped

#so a memoria local
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30), unique=True)
    
    #relação entre as duas tabelas,  one-to-many 
    #um usuario pode ter varias instancias de voz no banco para comparar
    voice: Mapped[list["Voice"]] = relationship(back_populates="user")

    #se um usuario so puder ter um audio de referencia:
    #voice: Mapped["Voice"] = relationship(back_populates="user")
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"



class Voice(Base):
    __tablename__ = "VoiceEnrollment"
    #não sei que outra informação vai ser posta aqui,
    #mas se for so isso, nao tem nem pra que duas tabelas
    #so um placeholder
    id: Mapped[int] = mapped_column(primary_key=True)
    voice_module: Mapped[str] = mapped_column(String(30))

    #conexão com a tabela de usuario
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="voice")
    

Base.metadata.create_all(engine)

#verifica se o email ja nao está cadastrado e se n estiver cria um novo usuario na tabela
def set_new_user(name, email):
    #abre uma conexão com o banco de dados
    #o session.begin() garante que será comitado quando a tarefa acabar
    with Session() as session, session.begin():
        #verifica se há um email igual
        slct = select(User).where(User.email == email)
        
        #retorna o primeiro usuario que encontrou ou nada
        if session.execute(slct).first() == None:
            slid = session.execute(select(User)).scalars().all()
            slid = len(slid)
            u1 = User(name = name, email = email, id = slid)
            session.add(u1)
        else:
            print("Usuario ja cadastrado")


#caso o usuario possa ter varias instancias de audio para comparar
#verificar se o email está cadastrado, salva o arquivo de audio no banco de dados
#e conecta com a tabela de usuario
def add_new_voice(audio, email):
    #praticamente o mesmo processo do set_new_user()
    with Session() as session, session.begin():
        slct = select(User).where(User.email == email)
        
        print(f"o tal do {session.execute(slct).scalars().first().name} tem {len(session.execute(slct).scalars().first().voice)} audios")

        if session.execute(slct).first() == None:
            print("Usuario não cadastrado")

        #colocar um limite de quantas instancias de audio o usuario pode cadastrar  
        elif len(session.execute(slct).scalars().first().voice) <= 5:
            slid = session.execute(select(Voice)).scalars().all()
            slid = len(slid)
            v1 = Voice(voice_module = audio, user = session.execute(slct).scalars().first(), id = slid)
            session.add(v1)
        else:
            print("Limite de audios alcançado")


# coloquei aqui mais como um placeholder     
# de novo verifica se o usuario existe ante de autenticar  
def autentication(audio, email):
    with Session() as session:
        slct = select(User).where(User.email == email)
        if session.execute(slct).first == None:
            print("Usuario não cadastrado")
        else:
            #processo de autenticação aí n sei como vai ser
            #tava pensando de ir procurando em todas as vozes
            #conectadas ao usuario ate achar um par
            #for voice_db in slct.voice:
            #   if audio == voice_db.voice_module:
            #       cadastrado lets go
            pass



#so pra testar e ver se ta tudo nos conformes
# set_new_user(name="Bedas", email="Bedas123@gmail.com")
# set_new_user(name="fotaine", email="fotin123@gmail.com")
# set_new_user(name="Dibas", email="Endibaberl@lascapedra.com")
# with Session() as session:
#     stmt = select(User)
#     res = session.execute(stmt)
#     fos = res.scalars().all()

#     for user in fos:
#         print(user.name, user.email)

# print("-------------------------------------------------------")
# add_new_voice(audio="voz do bedas", email="Bedas123@gmail.com")
# add_new_voice(audio="voz 2 bedaso", email="Bedas123@gmail.com")
# add_new_voice(audio="voz do fontaine", email="fotin123@gmail.com")
# add_new_voice(audio="voz do dibas", email="Endibaberl@lascapedra.com")

# with Session() as session:
#     slct = select(User)
#     res = session.execute(slct)
#     fos = res.scalars().all()
#     for user in fos:
#         for vc in user.voice:
#             print(vc.voice_module)