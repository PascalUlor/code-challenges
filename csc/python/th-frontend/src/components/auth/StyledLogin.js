import styled from 'styled-components';
import { white, dark, slateGrey } from '../~reuseables/variables/colors';
import { valera_round } from '../~reuseables/variables/font-famiy';

const FormContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  height: 100vh;
  justify-content: center;
  align-items: center;
  background-color: ${dark};
  h1 {
    font-family: 'Press Start 2P';
    width: 100%;
    text-align: center;
    font-size: 5rem;
    color: ${white};
  }
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 50%;
  height: 50vh;
  align-items: center;
  justify-content: center;

  h4 {
    font-family: 'Press Start 2P';
    color: ${white};
  }

  input {
    width: 50%;
    padding: 1rem;
    margin: 1rem;
    outline: none;
    border: none;
    font-family: ${valera_round};
  }

  button {
    background-color: ${slateGrey};
    color: ${white};
    font-size: 1.2rem;
    outline: none;
    border: none;
    padding: 0.3rem;

    &:hover {
    }
  }

  p {
    color: ${white};
    margin: 1rem 0;
    font-family: ${valera_round};
    font-size: 1rem;
  }
`;

export { FormContainer, Form };
