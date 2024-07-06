import { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

function Header() {
  const [isLogin, setIsLogin] = useState(false);

  return (
    <HeaderStyle>
      <Link to="/" className="logo">
        RAG Chatbot
      </Link>
      
      <nav className="auth">
        {isLogin && (
          <div>
            <Link to="logout" className="authLink">로그아웃</Link>
          </div>
        )}
        {!isLogin && (
          <div className="authLogin">
            <Link to="login" className="authLink">로그인</Link>
            <Link to="signup" className="authLink">회원가입</Link>
          </div>
        )}
        <Link to="history" className="authLink">History</Link>
        <Link to="manager" className="authLink">관리자 메뉴</Link>
      </nav>
    </HeaderStyle>
  );
};

const HeaderStyle = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  height: 60px;
  padding: 20px 40px;
  background: #333;

  .logo {
    color: white;
    font-size: 28px;
    font-weight: bold;
    text-decoration: none;
  }
  
  .auth {
    display: flex;
    gap: 10px;

    .authLogin {
      display: flex;
      gap: 10px;
    }
    .authLink {
      color: white;
      font-size: 14px;
      text-decoration: none;
    }
  }
`;

export default Header;