
# 🎤 MFCC e Autenticação por Voz

## 📌 Visão Geral

A autenticação por voz é uma técnica de biometria baseada em características únicas da fala de uma pessoa. Uma das abordagens mais comuns utiliza os **coeficientes cepstrais em escala Mel** (MFCCs) para extrair características relevantes da voz, combinados com modelos estatísticos como **GMM (Gaussian Mixture Models)**.

---

## 🎵 O que é MFCC?

**MFCC** (Mel-Frequency Cepstral Coefficients) são vetores de características que descrevem **como a voz soa ao ouvido humano**, focando nas propriedades acústicas da fala e ignorando o conteúdo falado.

---

## 🔬 Como o MFCC é Calculado?

### 1. Pré-Ênfase
Aumenta a energia nas altas frequências do sinal:
```python
y_pre_emphasized = np.append(y[0], y[1:] - 0.97 * y[:-1])
```

### 2. Framing
Divide o áudio em janelas de tempo (~20ms), pois o sinal de voz é não-estacionário.

### 3. Windowing (Hamming)
Evita distorções nas bordas aplicando uma janela de suavização:
```python
frame = frame * np.hamming(len(frame))
```

### 4. FFT (Transformada Rápida de Fourier)
Converte cada janela do tempo para o domínio da frequência.

### 5. Banco de Filtros Mel
Aplica filtros triangulares na escala Mel (semelhante à audição humana):
\[
f_{mel} = 2595 \cdot \log_{10}(1 + \frac{f}{700})
\]

### 6. Logaritmo
Simula a percepção logarítmica de volume humano.

### 7. DCT (Transformada Discreta do Cosseno)
Compacta a informação e remove redundâncias, mantendo os primeiros 12–13 coeficientes.

---

## ✅ Resultado

Um vetor de MFCC é gerado para cada janela (~25ms) do áudio. O áudio completo vira uma **sequência de vetores de características**, representando o timbre da voz.

---

## 🔐 Aplicação em Autenticação por Voz

### Por que MFCC?

- Independe do conteúdo falado.
- Representa características físicas da voz: trato vocal, cavidade nasal, cordas vocais.
- Ideal para sistemas biométricos.

---
# O que é GMM (Gaussian Mixture Model)

**GMM** significa **Gaussian Mixture Model** (Modelo de Mistura Gaussiana). É um modelo estatístico usado para representar uma distribuição de dados como uma **combinação de várias distribuições normais (gaussianas)**.

---

## 🌐 Intuição

Imagine que você tem um conjunto de dados espalhados. Em vez de usar uma única curva (uma gaussiana) para representar todos os dados, o GMM combina **várias curvas gaussianas** para descrever a distribuição dos dados de forma mais precisa.

---

## 🧮 Fórmula

Um GMM modela a distribuição de probabilidade \( p(x) \) como:

\[
p(x) = \sum_{k=1}^{K} \pi_k \cdot \mathcal{N}(x | \mu_k, \Sigma_k)
\]

Onde:

- \( K \) = número de componentes (gaussianas)
- \( \pi_k \) = peso do componente \( k \) (soma dos pesos = 1)
- \( \mu_k \), \( \Sigma_k \) = média e covariância da gaussiana \( k \)
- \( \mathcal{N}(x | \mu_k, \Sigma_k) \) = função densidade da normal multivariada

---

## 🧠 Aplicações

GMMs são usados em diversas áreas:

- 🎙️ **Reconhecimento de voz**: modelagem de características acústicas de sons ou locutores (**nosso objetivo**)
- 🖼️ **Visão computacional**: segmentação de imagens (fundo vs objeto)
- 📊 **Clustering (agrupamento)**: versão mais flexível do k-means
- 🚨 **Detecção de anomalias**

---

## ✅ Vantagens

- Flexível: modela distribuições complexas
- Não assume que os dados pertencem a um único cluster
- Útil quando há subgrupos naturais nos dados

---

## ⚙️ Treinamento (Algoritmo EM)

O GMM geralmente é treinado com o algoritmo **EM (Expectation-Maximization)**:

1. **E-step (Expectation)**: estima a probabilidade de cada ponto pertencer a cada gaussiana
2. **M-step (Maximization)**: atualiza os parâmetros das gaussianas com base nessas probabilidades


---

## 🧠 Pipeline: MFCC + GMM

### Etapas:

1. **Treinamento**
   - Captura de áudios do usuário.
   - Extração dos MFCCs.
   - Treinamento de um modelo **GMM (Gaussian Mixture Model)** com os vetores de MFCC.

2. **Verificação**
   - Novo áudio é capturado.
   - MFCCs são extraídos.
   - O GMM calcula a **verossimilhança** dos novos dados com o modelo do usuário.
   - Aceita ou rejeita a identidade com base na probabilidade.

### Representação:

```
[Áudio de entrada]
     ↓
[Extração de MFCCs]
     ↓
[Modelo GMM]
     ↓
[Verificação da identidade]
```

---


## 📚 Bibliotecas que podem ser utilizadas

- `librosa`: Extração de MFCCs
- `scikit-learn`: Modelagem com GMM
- `numpy`: Manipulação de arrays

---

## 📚 Referências

- [Desenvolvimento de um Sistema de Reconhecimento de Locutor Utilizando Aprendizado de Máquina - Henrique Hilleshein](https://wiki.sj.ifsc.edu.br/index.php/Desenvolvimento_de_um_Sistema_de_Reconhecimento_de_Locutor_Utilizando_Aprendizado_de_M%C3%A1quina)
- [Reconhecimento de Voz utilizando extração de Coeficientes Mel-Cepstrais e Redes Neurais Artificiais - Ernani Rodrigues de São Thiago ](https://wiki.sj.ifsc.edu.br/images/6/60/TCC290_Ernani_Rodrigues_de_S%C3%A3o_Thiago.pdf)
- [EXTRAÇÃO DE CARACTERÍSTICAS DO SINAL DE VOZ UTILIZANDO ANÁLISE FATORIAL VERDADEIRA - ADRIANO NOGUEIRA MATOS](https://tede.ufam.edu.br/bitstream/tede/2959/1/DISSERTACAO%20ADRIANO%20NOGUEIRA.pdf)
- [MFCC Implementation](https://www.kaggle.com/code/ilyamich/mfcc-implementation-and-tutorial)
- [Haytham Fayek – MFCC Explained](https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html)
- [Wikipedia: MFCC](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- [Scikit-learn Gaussian Mixture Models](https://scikit-learn.org/stable/modules/mixture.html)
