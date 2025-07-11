import React, { useState } from 'react'
import VoiceRecorder from './VoiceRecorder'
import Toast from './Toast'
import { voiceService } from '../services/api'
import '../styles/VoiceRegistration.css'

const VoiceRegistration = ({ userEmail, onComplete, onBack }) => {
  const [currentStep, setCurrentStep] = useState(1)
  const [recordings, setRecordings] = useState([null])
  const [isUploading, setIsUploading] = useState(false)
  const [toast, setToast] = useState(null)

  const totalSteps = 1

  const showToast = (message, type = 'error') => {
    setToast({ message, type })
    setTimeout(() => setToast(null), 5000)
  }

  const handleRecordingComplete = (audioBlob) => {
    if (audioBlob) {
      const newRecordings = [...recordings]
      newRecordings[currentStep - 1] = audioBlob
      setRecordings(newRecordings)
    }
  }

  const nextStep = () => {
    if (recordings[currentStep - 1]) {
      submitAllRecordings()
    } else {
      showToast('Complete a gravação antes de prosseguir')
    }
  }

  const submitAllRecordings = async () => {
    if (recordings[0] !== null) {
      setIsUploading(true)
      
      try {
        const audioFile = new File([recordings[0]], 'voice_registration.webm', {
          type: 'audio/webm;codecs=opus'
        })
        
        await voiceService.createVoiceProfile(userEmail, audioFile)
        showToast('Voz registrada com sucesso!', 'success')
        
        setTimeout(() => {
          if (onComplete) onComplete()
        }, 2000)
        
      } catch (error) {
        console.error('Error during voice registration:', error)
        const errorMessage = error.response?.data?.detail || 'Falha ao registrar voz. Tente novamente.'
        showToast(errorMessage, 'error')
      } finally {
        setIsUploading(false)
      }
    }
  }

  const getStepMessage = (step) => {
    return "Registre sua voz para autenticação"
  }

  const getStepInstruction = (step) => {
    return "Por favor, fale claramente: 'Olá, esta é minha voz para autenticação no sistema VIDA'"
  }

  return (
    <div className="voice-registration">
      <div className="registration-container">
        <header className="registration-header">
          <button 
            className="back-btn"
            onClick={onBack}
            disabled={isUploading}
          >
            ← Voltar
          </button>
          <h1>Registro de Voz</h1>
          <p>Configure seu perfil de voz para autenticação segura</p>
        </header>

        <div className="registration-content">
          <div className="step-info-card">
            <h2>{getStepMessage(currentStep)}</h2>
            <p className="step-instruction">{getStepInstruction(currentStep)}</p>
          </div>

          <VoiceRecorder
            key={currentStep}
            onRecordingComplete={handleRecordingComplete}
            maxDuration={5}
            disabled={isUploading}
          />

          <div className="registration-actions">
            <button 
              className="btn btn-primary btn-full"
              onClick={nextStep}
              disabled={!recordings[currentStep - 1] || isUploading}
            >
              {isUploading ? 'Registrando voz...' : 'Registrar Voz'}
            </button>
          </div>
        </div>
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

export default VoiceRegistration
