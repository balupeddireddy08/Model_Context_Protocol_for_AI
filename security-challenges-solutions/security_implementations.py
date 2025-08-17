"""
MCP Security Implementations

This module provides examples of security implementations for MCP servers and clients.
"""

import hashlib
import secrets
import time
import jwt
from typing import Dict, Any, Optional, Tuple


class MCPSecurity:
    """
    Base class for MCP security implementations.
    """
    
    @staticmethod
    def hash_password(password: str, salt: Optional[str] = None) -> Tuple[str, str]:
        """
        Hash a password using a secure hashing algorithm.
        
        Args:
            password (str): The password to hash
            salt (str, optional): The salt to use for hashing
            
        Returns:
            Tuple[str, str]: The hashed password and salt
        """
        if salt is None:
            salt = secrets.token_hex(16)
        
        # Use a strong hashing algorithm with multiple iterations
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        ).hex()
        
        return key, salt
    
    @staticmethod
    def verify_password(password: str, hashed_password: str, salt: str) -> bool:
        """
        Verify a password against a hashed password.
        
        Args:
            password (str): The password to verify
            hashed_password (str): The hashed password to verify against
            salt (str): The salt used for hashing
            
        Returns:
            bool: True if the password is valid, False otherwise
        """
        key, _ = MCPSecurity.hash_password(password, salt)
        return key == hashed_password


class JWTAuth:
    """
    JWT-based authentication for MCP.
    """
    
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        """
        Initialize JWT authentication.
        
        Args:
            secret_key (str): The secret key for JWT signing
            algorithm (str): The JWT algorithm to use
        """
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def generate_token(self, user_id: str, expiration: int = 3600) -> str:
        """
        Generate a JWT token.
        
        Args:
            user_id (str): The user ID to include in the token
            expiration (int): The token expiration time in seconds
            
        Returns:
            str: The generated JWT token
        """
        payload = {
            "sub": user_id,
            "iat": int(time.time()),
            "exp": int(time.time()) + expiration
        }
        
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Dict[str, Any]:
        """
        Verify a JWT token.
        
        Args:
            token (str): The token to verify
            
        Returns:
            Dict[str, Any]: The decoded token payload
        """
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.PyJWTError:
            raise ValueError("Invalid token")


class RateLimiter:
    """
    Rate limiting implementation for MCP.
    """
    
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        """
        Initialize rate limiter.
        
        Args:
            max_requests (int): Maximum requests allowed in the time window
            window_seconds (int): Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients = {}
    
    def is_allowed(self, client_id: str) -> bool:
        """
        Check if a client is allowed to make a request.
        
        Args:
            client_id (str): The client identifier
            
        Returns:
            bool: True if the client is allowed, False otherwise
        """
        current_time = time.time()
        
        # Initialize client if not exists
        if client_id not in self.clients:
            self.clients[client_id] = {
                "requests": 0,
                "window_start": current_time
            }
        
        client = self.clients[client_id]
        
        # Reset if window has expired
        if current_time - client["window_start"] > self.window_seconds:
            client["requests"] = 0
            client["window_start"] = current_time
        
        # Check if client has exceeded rate limit
        if client["requests"] >= self.max_requests:
            return False
        
        # Increment request count
        client["requests"] += 1
        return True


def sanitize_input(input_string: str) -> str:
    """
    Sanitize user input for security.
    
    Args:
        input_string (str): The input to sanitize
        
    Returns:
        str: The sanitized input
    """
    # TODO: Implement proper input sanitization
    # This is a very basic example and should be expanded for production use
    return input_string.replace("<", "&lt;").replace(">", "&gt;")
