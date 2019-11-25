import React, { useState } from 'react';
import axios from 'axios';
import { Redirect, Link } from 'react-router-dom';
import { Form, FormContainer } from './StyledLogin';

export default function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [retistrationSuccess, setRegistrationSuccess] = useState(false);
  const [registrationError, setRegistrationError] = useState({});

  const onSubmit = e => {
    e.preventDefault();
    const baseUrl = `https://mount-doom-mud.herokuapp.com`;

    axios
      .post(`${baseUrl}/api/registration/`, {
        username,
        password1: password,
        password2: confirmPassword
      })
      .then(res => {
        localStorage.setItem('key', res.data.key);
        setRegistrationSuccess(true);
      })
      .catch(err => setRegistrationError(err.response.data));
  };

  if (retistrationSuccess) {
    return <Redirect to="/" />;
  }

  if (Object.keys(registrationError).length > 0) {
    console.log(registrationError);
    if (registrationError.non_field_errors) {
      alert(registrationError.non_field_errors);
    }

    if (registrationError.username) {
      alert(registrationError.username);
    }

    if (registrationError.password) {
      alert(registrationError.password);
    }
    setRegistrationError(false);
    // alert(registrationError);
  }

  return (
    <FormContainer>
      <h1>Mud Game</h1>
      <Form onSubmit={onSubmit}>
        <h4>Register</h4>
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

        <input
          placeholder="Confirm Password"
          type="password"
          required
          onChange={e => setConfirmPassword(e.target.value)}
        />
        <button>Register</button>

        <p>
          Already have an account? <Link to="/login"> Login here</Link>
        </p>
      </Form>
    </FormContainer>
  );
}
