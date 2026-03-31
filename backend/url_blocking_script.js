// URL Blocking Script for Specific URLs
const BLOCKED_URLS = [
    "verification-urgent.com",
    "emergency-secure.com", 
    "lottery-winner.com",
    "virus-removal.com",
    "investment-guaranteed.com",
    "account-secure.com",
    "jobs-immediate.com",
    "deal-urgent.com",
    "verify-account.com",
    "payment-required.com"
];

function shouldBlockUrl(url) {
    return BLOCKED_URLS.some(blocked => url.includes(blocked));
}

function showBlockingPopup(url) {
    // Create popup overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    `;
    
    // Create popup content
    const content = document.createElement('div');
    content.style.cssText = `
        background: white;
        padding: 30px;
        border-radius: 10px;
        max-width: 400px;
        text-align: center;
    `;
    
    content.innerHTML = `
        <h2 style="color: #d32f2f; margin-bottom: 15px;">DANGEROUS URL BLOCKED</h2>
        <p style="margin-bottom: 20px;">This URL has been identified as dangerous and is blocked for your protection.</p>
        <div style="background: #f5f5f5; padding: 10px; border-radius: 5px; margin: 15px 0; font-family: monospace; word-break: break-all;">${url}</div>
        <button onclick="this.parentElement.parentElement.remove()" style="background: #d32f2f; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Stay Safe</button>
    `;
    
    overlay.appendChild(content);
    document.body.appendChild(overlay);
    
    // Remove popup when clicking overlay
    overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
            overlay.remove();
        }
    });
}

// Intercept all link clicks
document.addEventListener('click', function(e) {
    const link = e.target.closest('a');
    if (link && shouldBlockUrl(link.href)) {
        e.preventDefault();
        showBlockingPopup(link.href);
        return false;
    }
});

console.log('URL Blocking Script Loaded - Protected URLs:', BLOCKED_URLS.length);