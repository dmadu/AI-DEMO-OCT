import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Container, Paper } from '@mui/material';

const Home: React.FC = () => (
  <Container maxWidth="md" className="mt-10">
    <Paper elevation={3} className="p-8 text-center">
      <Typography variant="h4" component="h1" gutterBottom className="font-bold text-gray-800">
        Welcome to Public Home
      </Typography>
      <Typography variant="body1" className="text-gray-600 mb-6">
        This is the public home page of the application configured with React 19, TypeScript, Tailwind CSS, and Material UI.
      </Typography>
      <div className="flex justify-center gap-4">
        <Button variant="contained" color="primary" component={Link} to="/login">
          Go to Login
        </Button>
        <Button variant="outlined" color="primary" component={Link} to="/dashboard">
          Go to Dashboard
        </Button>
      </div>
    </Paper>
  </Container>
);

const Login: React.FC = () => (
  <Container maxWidth="xs" className="mt-20">
    <Paper elevation={3} className="p-6">
      <Typography variant="h5" component="h1" align="center" gutterBottom className="font-semibold">
        Login Redirect
      </Typography>
      <Typography variant="body2" align="center" className="text-gray-500 mb-6">
        Placeholder login view. Authentication workflows will be connected here.
      </Typography>
      <div className="flex flex-col gap-4">
        <Button variant="contained" color="primary" fullWidth component={Link} to="/dashboard">
          Simulate Login to Dashboard
        </Button>
        <Button variant="text" color="secondary" fullWidth component={Link} to="/">
          Back to Home
        </Button>
      </div>
    </Paper>
  </Container>
);

const Dashboard: React.FC = () => (
  <Container maxWidth="lg" className="mt-10">
    <Paper elevation={2} className="p-6">
      <Typography variant="h4" component="h1" gutterBottom className="font-bold text-indigo-700">
        Dashboard View
      </Typography>
      <Typography variant="body1" className="text-gray-700 mb-4">
        You have successfully accessed the authenticated dashboard placeholder.
      </Typography>
      <div className="flex gap-4">
        <Button variant="contained" color="secondary" component={Link} to="/">
          Logout / Home
        </Button>
      </div>
    </Paper>
  </Container>
);

export const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" className="flex-grow font-semibold">
            React 19 MUI Tailwind App
          </Typography>
          <Button color="inherit" component={Link} to="/">
            Home
          </Button>
          <Button color="inherit" component={Link} to="/login">
            Login
          </Button>
          <Button color="inherit" component={Link} to="/dashboard">
            Dashboard
          </Button>
        </Toolbar>
      </AppBar>
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </main>
    </div>
  );
};

export default App;
