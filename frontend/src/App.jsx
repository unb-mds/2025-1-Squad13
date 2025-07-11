import React, { useState, useEffect } from 'react'
import WelcomeScreen from './components/WelcomeScreen'
import RegisterScreen from './components/RegisterScreen'
import VoiceLogin from './components/VoiceLogin'
import VoiceRegistration from './components/VoiceRegistration'
import SuccessScreen from './components/SuccessScreen'
import ErrorScreen from './components/ErrorScreen'
import './styles/App.css'

function App() {
  const [currentScreen, setCurrentScreen] = useState('welcome')
  const [screenData, setScreenData] = useState({})

  const screenTitles = {
    'welcome': 'Bem-vindo | VIDA',
    'register': 'Registro | VIDA',
    'voice-login': 'Login por Voz | VIDA',
    'voice-registration': 'Registro de Voz | VIDA',
    'success': 'Sucesso | VIDA',
    'error': 'Erro | VIDA'
  }

  useEffect(() => {
    document.title = screenTitles[currentScreen] || 'VIDA'
  }, [currentScreen])

  const navigateToScreen = (screen, data = {}) => {
    setCurrentScreen(screen)
    setScreenData(data)
  }

  const handleVoiceLoginSuccess = (data) => {
    navigateToScreen('success', {
      type: 'voice-login',
      message: '',
      email: data.email,
      verification: data.verification
    })
  }

  const handleVoiceRegistrationComplete = () => {
    navigateToScreen('success', {
      type: 'voice-registration',
      message: 'Perfil de voz configurado com sucesso!',
      email: screenData.email
    })
  }

  const renderScreen = () => {
    switch (currentScreen) {
      case 'welcome':
        return <WelcomeScreen onNavigate={navigateToScreen} />
      case 'register':
        return <RegisterScreen onNavigate={navigateToScreen} />
      case 'voice-login':
        return <VoiceLogin onNavigate={navigateToScreen} onSuccess={handleVoiceLoginSuccess} />
      case 'voice-registration':
        return (
          <VoiceRegistration 
            userEmail={screenData.email}
            onComplete={handleVoiceRegistrationComplete}
            onBack={() => navigateToScreen('welcome')}
          />
        )
      case 'success':
        return <SuccessScreen onNavigate={navigateToScreen} data={screenData} />
      case 'error':
        return <ErrorScreen onNavigate={navigateToScreen} data={screenData} />
      default:
        return <WelcomeScreen onNavigate={navigateToScreen} />
    }
  }

  return (
    <div className="app">
      {renderScreen()}
    </div>
  )
}

export default App
