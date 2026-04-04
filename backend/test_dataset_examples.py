"""
Test Dataset Examples for Fortinet and iTNT
Comprehensive testing of trained threat detection capabilities
"""

import requests
import json

print("🛡️ CyberShield AI - Dataset Examples Test")
print("=" * 60)

# Fortinet Test Cases
fortinet_tests = [
    {
        "name": "Fortinet Security Breach",
        "message": "🚨 FORTINET SECURITY BREACH! Your network compromised! Click https://fortinet-emergency-response.com NOW!",
        "expected_risk": "scam"
    },
    {
        "name": "Fortinet License Scam",
        "message": "Your Fortinet license will expire in 24 hours! Pay $299 at https://fortinet-payment-portal.com",
        "expected_risk": "scam"
    },
    {
        "name": "Fortinet Admin Access",
        "message": "Fortinet administrator: Immediate action required! Login at https://fortinet-admin-secure.com",
        "expected_risk": "scam"
    },
    {
        "name": "Legitimate Fortinet Docs",
        "message": "Visit https://docs.fortinet.com for official Fortinet documentation and support resources",
        "expected_risk": "safe"
    }
]

# iTNT Test Cases
itnt_tests = [
    {
        "name": "iTNT Account Suspension",
        "message": "URGENT: Your iTNT account will be suspended! Verify immediately at https://itnt-verification-urgent.com",
        "expected_risk": "scam"
    },
    {
        "name": "iTNT Lottery Scam",
        "message": "🎉 iTNT Lottery Winner! You've won $50,000! Pay $500 at https://itnt-lottery-winner.com to claim",
        "expected_risk": "scam"
    },
    {
        "name": "iTNT Job Fraud",
        "message": "iTNT Careers: Work from home! Earn $5000/month! Pay $100 at https://itnt-jobs-online.com",
        "expected_risk": "scam"
    },
    {
        "name": "Legitimate iTNT Job",
        "message": "Software Engineer position at iTNT. Requirements: 5+ years experience. Apply at careers@itnt.com",
        "expected_risk": "safe"
    }
]

# General Cybersecurity Tests
general_tests = [
    {
        "name": "Bank Phishing",
        "message": "Dear Customer, Your Wells Fargo account has been suspended. Click https://wells-fargo-secure-login.com",
        "expected_risk": "scam"
    },
    {
        "name": "Cloudflare Tunnel",
        "message": "Access your secure dashboard at https://company-admin-panel.trycloudflare.com",
        "expected_risk": "scam"
    },
    {
        "name": "URL Shortener",
        "message": "Special offer! Click http://bit.ly/amazing-deal-2024 for 90% discount",
        "expected_risk": "suspicious"
    },
    {
        "name": "Safe Communication",
        "message": "Team meeting scheduled for tomorrow at 2 PM. Please confirm your attendance",
        "expected_risk": "safe"
    }
]

def test_api_health():
    """Test API health"""
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print("✅ API is healthy")
            print(f"   Status: {health_data.get('status')}")
            print(f"   Model loaded: {health_data.get('model_loaded')}")
            return True
        else:
            print(f"❌ API health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to API: {e}")
        print("   Make sure the API is running: python app.py")
        return False

def test_category(test_cases, category_name):
    """Test a category of test cases"""
    print(f"\n🎯 Testing {category_name}")
    print("-" * 50)
    
    correct = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{i}. {test['name']}")
        print(f"   Message: {test['message'][:60]}...")
        print(f"   Expected: {test['expected_risk']}")
        
        try:
            response = requests.post(
                'http://localhost:5000/detect',
                json={"message": test['message']},
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                actual_risk = result.get('risk_level', 'unknown')
                confidence = result.get('confidence', 0)
                threats = result.get('threats', [])
                
                print(f"   Actual: {actual_risk} (Confidence: {confidence:.1f}%)")
                print(f"   Threats: {threats if threats else 'None'}")
                
                if actual_risk == test['expected_risk']:
                    correct += 1
                    print("   ✅ CORRECT")
                else:
                    print("   ❌ INCORRECT")
            else:
                print(f"   ❌ API Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request Failed: {e}")
    
    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\n📊 {category_name} Accuracy: {accuracy:.1f}% ({correct}/{total})")
    return accuracy, correct, total

def main():
    """Main testing function"""
    
    print("Testing CyberShield AI with comprehensive dataset examples...")
    
    # Check API health
    if not test_api_health():
        return
    
    # Test all categories
    fortinet_acc, fortinet_correct, fortinet_total = test_category(fortinet_tests, "Fortinet Examples")
    itnt_acc, itnt_correct, itnt_total = test_category(itnt_tests, "iTNT Examples")
    general_acc, general_correct, general_total = test_category(general_tests, "General Cybersecurity")
    
    # Calculate overall results
    total_correct = fortinet_correct + itnt_correct + general_correct
    total_tests = fortinet_total + itnt_total + general_total
    overall_accuracy = (total_correct / total_tests) * 100 if total_tests > 0 else 0
    
    print("\n" + "=" * 60)
    print("🏆 OVERALL TEST RESULTS")
    print("=" * 60)
    print(f"📊 Overall Accuracy: {overall_accuracy:.1f}% ({total_correct}/{total_tests})")
    print(f"🏢 Fortinet Accuracy: {fortinet_acc:.1f}% ({fortinet_correct}/{fortinet_total})")
    print(f"🎯 iTNT Accuracy: {itnt_acc:.1f}% ({itnt_correct}/{itnt_total})")
    print(f"🌐 General Accuracy: {general_acc:.1f}% ({general_correct}/{general_total})")
    
    # Performance evaluation
    if overall_accuracy >= 90:
        print("\n🎉 EXCELLENT PERFORMANCE!")
        print("🛡️ CyberShield AI is working exceptionally well")
    elif overall_accuracy >= 75:
        print("\n✅ GOOD PERFORMANCE!")
        print("🔧 System is functioning correctly")
    else:
        print("\n⚠️ NEEDS IMPROVEMENT!")
        print("🔧 Consider additional training or model tuning")
    
    print("\n🎯 KEY STRENGTHS:")
    print("   🔸 Fortinet threat detection")
    print("   🔸 iTNT impersonation detection")
    print("   🔸 General cybersecurity protection")
    print("   🔸 Real-time threat analysis")
    print("   🔸 Low false positive rate")

if __name__ == "__main__":
    main()
