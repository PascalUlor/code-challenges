import React from "react";
import styled from "styled-components";
import PropTypes from "prop-types";
import { forestGreen } from "../variables";

const TextArea = ({ name, value, onChange }) => (
  <>
    <StyledTextBox
      name={name}
      value={value}
      onChange={onChange}
      placeholder="Say Something..."
    />
  </>
);

const StyledTextBox = styled.textarea`
  background: transparent;
  border: 5px solid ${forestGreen};
  color: white;
  font-weight: 500;
  background: transparent;
    border: none;
    color: white;
    outline: 0;
    width: 100%;
    box-sizing: border-box;
`;

TextArea.propTypes = {
  id: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  rows: PropTypes.string.isRequired,
  className: PropTypes.string.isRequired
};

export default TextArea;
