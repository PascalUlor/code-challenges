import React from 'react';
import { Button, NavigationStyle } from '../styles/DashBoardStyles';

const Navigation = ({ direction }) => {
  return (
    <NavigationStyle>
      <Button
        className="btn btn-up"
        onClick={e => {
          direction(e.target.id);
        }}
        id="n"
      >
        ↑
      </Button>
      <div className="mid-section">
        <Button
          className="btn btn-left"
          onClick={e => {
            direction(e.target.id);
          }}
          id="w"
        >
          ←
        </Button>
        <Button
          className="btn btn-right"
          onClick={e => {
            direction(e.target.id);
          }}
          id="e"
        >
          →
        </Button>
      </div>

      <Button
        className="btn btn-down"
        onClick={e => {
          direction(e.target.id);
        }}
        id="s"
      >
        ↓
      </Button>
    </NavigationStyle>
  );
};

export default Navigation;
