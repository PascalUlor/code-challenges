import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import PrivateRoute from "./components/~reuseables/molecules/PrivateRoute";
import GameArea from "./components/views/GameArea";

function App() {
  return (
      <div className="App">
        <Router>
          <Route exact path="/login" component={Login} />
          <Route exact path="/register" component={Register} />
          <PrivateRoute exact path="/" component={GameArea} />
        </Router>
      </div>
  );
}

export default App;
