import React, { useState } from 'react';
import axios from 'axios';
import { Redirect, Link } from 'react-router-dom';
import { Form, FormContainer } from './StyledLogin';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginSuccess, setLoginSuccess] = useState(false);
  const [loginError, setLoginError] = useState(false);

  const onSubmit = e => {
    e.preventDefault();
    const baseUrl = `https://mount-doom-mud.herokuapp.com`;
    axios
      .post(`${baseUrl}/api/login/`, {
        username,
        password
      })
      .then(res => {
        localStorage.setItem('key', res.data.key);
        setLoginSuccess(res.data);
        console.log(res);
      })
      .catch(err => {
        setLoginError(err.response.data.non_field_errors[0]);
      });
  };

  if (loginSuccess) {
    return <Redirect to="/" />;
  }

  if (loginError) {
    alert(loginError);
    setLoginError(false);
  }

  return (
    <FormContainer>
      <h1>Mud Game</h1>
      <Form onSubmit={onSubmit}>
        <h4>Login</h4>
        <input
          placeholder="Enter Username"
          type="text"
          required
          onChange={e => setUsername(e.target.value)}
        />
        <input
          placeholder="Enter Password"
          type="password"
          required
          onChange={e => setPassword(e.target.value)}
        />
        <button>Login</button>
        <p>Don't have an account? <Link to="/register"> Register here</Link></p>
      </Form>
    </FormContainer>
  );
}
