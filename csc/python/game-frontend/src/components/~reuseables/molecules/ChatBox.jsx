import React, { useState } from 'react';
import { StyledForm } from '../styles/DashBoardStyles';
// import TextArea from '../atoms/TextArea';
import styled from 'styled-components';
import { forestGreen } from '../variables/colors';

const StyledInput = styled.input`
  color: white;
  font-weight: 500;
  background: transparent;
  border: 1px dotted ${forestGreen};
  color: white;
  outline: 0;
  padding: 1rem;
  width: 100%;
  margin-top: 1rem;
`;

const ChatBox = ({ sendMessage }) => {
  const [userInput, setUserInput] = useState("");

  const handleInputChange = e => {
    setUserInput(e.target.value);
  };

  const handleSubmit =(e)=>{
    e.preventDefault();
    sendMessage(userInput)
    setUserInput('');
    
  }
  
  return (
    <StyledForm>
      <button onClick={() => {localStorage.removeItem('key'); window.location.reload()}}>Logout</button>
      <form onSubmit={handleSubmit}>
      <StyledInput name="message" placeholder="Enter chat here"
      value={userInput}
      onChange={handleInputChange}/>
      <input type="submit" style={{display:"none"}}/>
      </form>
    </StyledForm>
  );
};

export default ChatBox;
