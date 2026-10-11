import React, { useEffect, useState } from 'react';
import { Container, Typography, Box, Paper, CircularIndicator } from '@mui/material';

function App() {
  const [health, setHealth] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => {
        setHealth(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Full Stack Application
        </Typography>
        <Paper elevation={3} sx={{ p: 4, mt: 2 }}>
          <Typography variant="h6" gutterBottom>
            Backend Health Status:
          </Typography>
          {loading ? (
            <Typography>Loading...</Typography>
          ) : (
            <pre style={{ background: '#f4f4f4', padding: '10px' }}>
              {JSON.stringify(health, null, 2)}
            </pre>
          )}
        </Paper>
      </Box>
    </Container>
  );
}

export default App;
