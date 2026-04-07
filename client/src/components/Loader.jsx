import React from 'react';

function Loader() {
  return (
    <div className="loader-container">
      <div className="loader">
        <div className="loader-book">
          <div className="loader-page"></div>
          <div className="loader-page"></div>
          <div className="loader-page"></div>
        </div>
        <p className="loader-text">Loading...</p>
      </div>
    </div>
  );
}

export default Loader;
