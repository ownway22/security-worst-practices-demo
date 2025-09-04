// Intentionally insecure Node.js server
const http = require('http');
const { exec } = require('child_process');

// Hard-coded fake secrets
const stripeApiKey = 'sk_live_FAKE_insecure_key_123456789';
const privateKey = `-----BEGIN RSA PRIVATE KEY-----\nFAKEINSECUREKEYDATA\n-----END RSA PRIVATE KEY-----`;

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  if (url.pathname === '/exec') {
    const cmd = url.searchParams.get('cmd') || 'echo hello';
    // Command injection vulnerability
    exec(cmd, (err, stdout, stderr) => {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(stdout || stderr || (err && err.message));
    });
  } else if (url.pathname === '/eval') {
    const code = url.searchParams.get('code') || '2+2';
    // Arbitrary code execution
    const result = eval(code); // insecure use of eval
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(String(result));
  } else {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Insecure demo server');
  }
});

server.listen(3000, '0.0.0.0', () => {
  console.log('Insecure server listening on port 3000');
});
