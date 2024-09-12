const brokenLinkSVG = `<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M17 7h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1 0 1.43-.98 2.63-2.31 2.98l1.46 1.46C20.88 15.61 22 13.95 22 12c0-2.76-2.24-5-5-5zm-1 4h-2.19l2 2H16zM2 4.27l3.11 3.11C3.29 8.12 2 9.91 2 12c0 2.76 2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1 0-1.59 1.21-2.9 2.76-3.07L8.73 11H8v2h2.73L13 15.27V17h1.73l4.01 4L20 19.74 3.27 3 2 4.27z"/></svg>`;
const linkSVG = `<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" fill="currentColor"><path d="M0 0h24v24H0z" fill="none"/><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>`;

function isAllowedEnvironment() {
    const currentUrl = window.location.href;
    return currentUrl.includes('127.0.0.1') || (currentUrl.startsWith('https://docs-dev') && currentUrl.includes("/learn/"))
}

document.addEventListener('DOMContentLoaded', function() {
    if (!isAllowedEnvironment()) {
        return; // Exit early if not in allowed environment
    }
    const headerEllipsis = document.querySelector('.md-header__ellipsis');

    if (headerEllipsis) {
        const walletButton = document.createElement('button');
        walletButton.className = 'md-button md-button--primary md-header__button wallet-button';
        walletButton.style.float = 'right';
        walletButton.style.fontSize = 'small';
        walletButton.style.lineHeight = "24px";
        walletButton.addEventListener('click', handleWalletAction);
        
        const buttonText = document.createElement('span');
        buttonText.className = 'wallet-button-text';
        buttonText.textContent = 'Connect Wallet';
        walletButton.appendChild(buttonText);
        
        const buttonIcon = document.createElement('span');
        buttonIcon.className = 'wallet-button-icon';
        buttonIcon.innerHTML = linkSVG
        buttonIcon.style.display = 'none';
        walletButton.appendChild(buttonIcon);
        
        headerEllipsis.appendChild(walletButton);
        
        const style = document.createElement('style');
        style.textContent = `
            @media screen and (max-width: 465px) {
                .wallet-button-text { display: none; }
                .wallet-button-icon { display: inline !important; }
            }
        `;
        document.head.appendChild(style);

        const savedAddress = localStorage.getItem('walletAddress');
        if (savedAddress) {
            updateButtonState(true, savedAddress);
        }
    }
});

async function handleWalletAction() {
    const button = document.querySelector('.wallet-button');
    const buttonText = button.querySelector('.wallet-button-text');
    if (buttonText.textContent.startsWith('Connect')) {
        await connectWallet();
    } else {
        await disconnectWallet();
    }
}

async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected successfully');
            localStorage.setItem('walletAddress', accounts[0]);
            updateButtonState(true, accounts[0]);
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            updateButtonState(false);
        }
    } else {
        console.log('Please install MetaMask or another Ethereum wallet');
        alert('Please install MetaMask or another Ethereum wallet');
    }
}

async function disconnectWallet() {
    console.log('Wallet disconnected');
    localStorage.removeItem('walletAddress');
    updateButtonState(false);
}

function updateButtonState(connected, address = '') {
    const button = document.querySelector('.wallet-button');
    const buttonText = button.querySelector('.wallet-button-text');
    const buttonIcon = button.querySelector('.wallet-button-icon');
    if (button) {
        if (connected) {
            const abbreviatedAddress = `${address.slice(0, 4)}..${address.slice(-4)}`;
            buttonText.textContent = `Disconnect ${abbreviatedAddress}`;
            buttonIcon.innerHTML = brokenLinkSVG;
            button.classList.remove('md-button--primary');
            button.classList.add('md-button--accent');
        } else {
            buttonText.textContent = 'Connect Wallet';
            buttonIcon.innerHTML = linkSVG;
            button.classList.add('md-button--primary');
            button.classList.remove('md-button--accent');
        }
    }
}

// Listen for account changes
if (typeof window.ethereum !== 'undefined') {
    window.ethereum.on('accountsChanged', function (accounts) {
        if (accounts.length === 0) {
            // User disconnected their wallet
            disconnectWallet();
        } else {
            // User switched to a different account
            localStorage.setItem('walletAddress', accounts[0]);
            updateButtonState(true, accounts[0]);
        }
    });
}
