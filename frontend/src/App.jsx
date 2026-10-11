import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Container, Card, CardContent } from '@mui/material';
import DashboardIcon from '@mui/icons-material/Dashboard';
import HomeIcon from '@mui/icons-material/Home';

function Home() {
  return (
    <div className="space-y-6">
      <div className="p-6 bg-white rounded-lg shadow-md border border-gray-200">
        <h1 className="text-3xl font-bold text-indigo-600 mb-2">Welcome to React 19 & MUI Application</h1>
        <p className="text-gray-600">
          This platform combines Tailwind CSS for utility-first styling and Material UI for robust interactive components.
        </p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="hover:shadow-lg transition-shadow">
          <CardContent>
            <Typography variant="h6" className="font-bold text-gray-800 mb-2">
              Tailwind CSS
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Rapidly build modern designs without ever leaving your HTML.
            </Typography>
          </CardContent>
        </Card>
        
        <Card className="hover:shadow-lg transition-shadow">
          <CardContent>
            <Typography variant="h6" className="font-bold text-gray-800 mb-2">
              Material UI
            </Typography>
            <Typography variant="body2" color="text.secondary">
              React components for faster and easier web development.
            </Typography>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow">
          <CardContent>
            <Typography variant="h6" className="font-bold text-gray-800 mb-2">
              React Router
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Declarative routing for React web applications.
            </Typography>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

function Dashboard() {
  return (
    <div className="p-6 bg-white rounded-lg shadow-md border border-gray-200">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Dashboard Overview</h2>
      <p className="text-gray-600">System operational status: All services running normally.</p>
    </div>
  );
}

export default function App() {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <AppBar position="static" elevation={1} className="bg-indigo-700">
        <Toolbar className="flex justify-between">
          <Typography variant="h6" component="div" className="font-bold tracking-wide">
            Enterprise SPA
          </Typography>
          <div className="space-x-2">
            <Button color="inherit" component={Link} to="/" startIcon={<HomeIcon />}>
              Home
            </Button>
            <Button color="inherit" component={Link} to="/dashboard" startIcon={<DashboardIcon />}>
              Dashboard
            </Button>
          </div>
        </Toolbar>
      </AppBar>

      <Container maxWidth="lg" className="my-8 flex-grow">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Container>

      <footer className="py-4 text-center text-sm text-gray-500 border-t bg-white">
        &copy; {new Date().getFullYear()} Enterprise Full-Stack Application. All rights reserved.
      </footer>
    </div>
  );
}
