import styled from "styled-components";

function Footer() {
  return (
    <FooterStyle>
      <div className="copyright">
      © 2024 RAG Chatbot. All rights reserved.
      </div>
    </FooterStyle>
  )
};

const FooterStyle = styled.footer`
  padding: 24px 0;
  background: #333;

  .copyright {
    color: white;
    font-size: 12px;
    text-align: center;
  }
`;

export default Footer;