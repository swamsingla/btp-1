import React from 'react';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-inner">
        <div className="footer-left">
          <Link to="/" className="footer-brand">
            <span>📚</span> NCERT Smart Wiki
          </Link>
          <p>A multilingual knowledge platform for students in grades 6–12, converting NCERT textbooks into an accessible digital encyclopedia.</p>
        </div>
        <div className="footer-right">
          <div className="footer-section">
            <h4>Languages</h4>
            <p>English • हिन्दी • తెలుగు • ଓଡ଼ିଆ</p>
          </div>
          <div className="footer-section">
            <h4>Technology</h4>
            <p>React • Express • MongoDB • KaTeX</p>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <p>Built with ❤️ for Indian Education &nbsp;•&nbsp; Powered by NCERT Curriculum</p>
      </div>
    </footer>
  );
}

export default Footer;
