import React from 'react';

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-100">
      <div className="bg-white p-8 rounded-xl shadow-md max-w-md w-full text-center">
        <h1 className="text-3xl font-bold text-slate-800 mb-4">React 19 Frontend</h1>
        <p className="text-slate-600 mb-6">
          Monorepo environment successfully initialized with React 19, Flask, PostgreSQL 16, and Nginx.
        </p>
        <div className="inline-block px-4 py-2 bg-emerald-100 text-emerald-800 rounded-lg font-medium">
          System Operational
        </div>
      </div>
    </div>
  );
}

export default App;
