import React from 'react'
import '../styles/SuccessScreen.css'

const SuccessScreen = ({ onNavigate, data }) => {
  const isLogin = data.type === 'voice-login'
  
  return (
    <main className="success-screen">
      <div className="success-container">
        <div className="success-icon">
          <div className="checkmark">✓</div>
        </div>
        
        <header className="success-header">
          <h1>Sucesso!</h1>
          {data.message && <p>{data.message}</p>}
          {data.name && <p className="welcome-text">Bem-vindo(a), {data.name}!</p>}
          {data.email && <p className="email-text">Logado como: {data.email}</p>}
        </header>

        <section className="success-actions">
          {isLogin ? (
            <>
              <button 
                className="btn btn-primary"
                onClick={() => onNavigate('welcome')}
              >
                Voltar para o Início
              </button>
            </>
          ) : (
            <>
              <button 
                className="btn btn-primary"
                onClick={() => onNavigate('welcome')}
              >
                Sair
              </button>
            </>
          )}
        </section>
      </div>
    </main>
  )
}

export default SuccessScreen
