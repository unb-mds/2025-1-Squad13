import React, { useState } from 'react'
import VoiceRecorder from './VoiceRecorder'
import FormInput from './FormInput'
import Toast from './Toast'
import { voiceService } from '../services/api'
import '../styles/VoiceLogin.css'

const VoiceLogin = ({ onNavigate, onSuccess }) => {
  const [email, setEmail] = useState('')
  const [voiceBlob, setVoiceBlob] = useState(null)
  const [isVerifying, setIsVerifying] = useState(false)
  const [toast, setToast] = useState(null)
  const [step, setStep] = useState('voice')

  const showToast = (message, type = 'error') => {
    setToast({ message, type })
    setTimeout(() => setToast(null), 5000)
  }

  const handleVoiceRecording = (audioBlob) => {
    setVoiceBlob(audioBlob)
  }

  const handleVoiceSubmit = async () => {
    if (!voiceBlob) {
      showToast('Grave sua voz primeiro')
      return
    }

    if (!email) {
      showToast('Digite seu email primeiro')
      return
    }

    setIsVerifying(true)
    
    try {
      // Convert blob to file
      const audioFile = new File([voiceBlob], 'voice_login.webm', {
        type: 'audio/webm;codecs=opus'
      })
      
      // Verify voice with backend
      const result = await voiceService.verifyVoice(email, audioFile)
      
      if (result.verified) {
        setTimeout(() => {
          if (onSuccess) {
            onSuccess({
              email,
              verification: result
            })
          }
        }, 500)
      } else {
        showToast(`Verificação de voz falhou. Confiança: ${(result.score * 100).toFixed(1)}%`)
        setVoiceBlob(null)
      }
      
    } catch (error) {
      console.error('Voice verification error:', error)
      const errorMessage = error.response?.data?.detail || 'Verificação de voz falhou. Tente novamente.'
      showToast(errorMessage)
      setVoiceBlob(null)
    } finally {
      setIsVerifying(false)
    }
  }



  return (
    <div className="voice-login">
      <div className="voice-login-container">
        <header className="voice-login-header">
          <button 
            className="back-btn"
            onClick={() => onNavigate('welcome')}
            disabled={isVerifying}
          >
            ← Voltar
          </button>
          <h1>Login por Voz</h1>
          <p>Faça login usando sua voz</p>
        </header>

        <section className="voice-step">
          <div className="step-info">
            <h2>Autenticação por Voz</h2>
            <p>Digite seu email e grave sua voz para fazer login</p>
          </div>

          <div className="email-input">
            <FormInput
              label="Email"
              type="email"
              name="email"
              value={email}
              onChange={(name, value) => setEmail(value)}
              placeholder="Digite seu email"
              required
            />
          </div>
          
          <div className="voice-instructions">
            <div className="instruction-card">
              <span className="instruction-icon">🎯</span>
              <p>Fale claramente e naturalmente</p>
            </div>
            <div className="instruction-card">
              <span className="instruction-icon">🔊</span>
              <p>Use o mesmo tom do registro</p>
            </div>
            <div className="instruction-card">
              <span className="instruction-icon">🎤</span>
              <p>Garanta um ambiente silencioso</p>
            </div>
          </div>
          
          <VoiceRecorder
            onRecordingComplete={handleVoiceRecording}
            maxDuration={5}
            disabled={isVerifying}
          />
          
          <div className="voice-actions">
            <button 
              className="btn btn-primary"
              onClick={handleVoiceSubmit}
              disabled={!voiceBlob || !email || isVerifying}
            >
              {isVerifying ? 'Verificando Voz...' : 'Fazer Login'}
            </button>
          </div>
        </section>

        <footer className="voice-login-footer">
          <p>
            Não tem uma conta?{' '}
            <button 
              className="link-btn"
              onClick={() => onNavigate('register')}
              disabled={isVerifying}
            >
              Registre-se aqui
            </button>
          </p>
        </footer>
      </div>
      
      {toast && (
        <Toast 
          message={toast.message} 
          type={toast.type}
          onClose={() => setToast(null)}
        />
      )}
    </div>
  )
}

export default VoiceLogin
