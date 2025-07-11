#!/usr/bin/env node

// Script para testar a API diretamente (sem CORS)
const https = require('https');

const testAPI = () => {
  const options = {
    hostname: 'vida-project-api.fly.dev',
    port: 443,
    path: '/health',
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
  };

  const req = https.request(options, (res) => {
    console.log(`Status: ${res.statusCode}`);
    console.log(`Headers:`, res.headers);

    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });

    res.on('end', () => {
      console.log('Response:', data);
    });
  });

  req.on('error', (e) => {
    console.error(`Erro: ${e.message}`);
  });

  req.end();
};

console.log('Testando API...');
testAPI();
