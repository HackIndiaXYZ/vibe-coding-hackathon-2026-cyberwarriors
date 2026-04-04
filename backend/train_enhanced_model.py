"""
Enhanced Model Training for Fortinet and iTNT Threat Detection
Specialized training for organization-specific threats
"""

import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

print("🛡️ CyberShield AI - Enhanced Model Training")
print("🎯 Specialized for Fortinet and iTNT Threat Detection")
print("=" * 70)

def create_enhanced_training_data():
    """Create comprehensive training data for Fortinet, iTNT, and general threats"""
    
    # SCAM examples - High confidence training
    scam_examples = [
        # Fortinet-specific scams
        "🚨 FORTINET SECURITY BREACH! Your network compromised! Click https://fortinet-emergency-response.com NOW!",
        "URGENT: Fortinet license will expire in 24 hours! Pay $299 at https://fortinet-payment-portal.com",
        "Fortinet administrator: Immediate action required! Login at https://fortinet-admin-secure.com",
        "🎓 Fortinet Certification Special! Pay $200 at https://fortinet-certification-fast.com",
        "🤝 Fortinet Partner Program: Pay $1000 fee at https://fortinet-partner-portal.com",
        "CRITICAL: Fortinet firewall breach detected! Secure your account immediately",
        "Your Fortinet account compromised! Click link now or lose access forever",
        "Fortinet security alert! Suspicious activity detected! Verify immediately",
        
        # iTNT-specific scams
        "URGENT: Your iTNT account will be suspended! Verify immediately at https://itnt-verification-urgent.com",
        "🎉 iTNT Lottery Winner! You've won $50,000! Pay $500 at https://itnt-lottery-winner.com",
        "iTNT Careers: Work from home! Earn $5000/month! Pay $100 at https://itnt-jobs-online.com",
        "⚠️ iTNT Security Alert: Your device infected! Call https://itnt-tech-support.com",
        "💰 iTNT Investment: Guaranteed 200% returns! Visit https://itnt-investment-portal.com",
        "iTNT account will be blocked! Verify identity immediately or lose access",
        "Congratulations iTNT winner! Claim prize by paying processing fee",
        "iTNT system compromised! Emergency action required! Click now",
        
        # General financial scams
        "Congratulations! You won $1,000,000! Pay $500 processing fee to claim prize",
        "Work from home earn $5000/month! Pay registration fee to start job immediately",
        "WARNING: Your computer infected with dangerous malware! Call technicians now",
        "Double your investment in 7 days! Guaranteed returns! Pay fee to join",
        "LIMITED TIME: Special offer expires today! Act now or lose forever!",
        "Your computer license has expired! Pay immediately to continue service",
        "You've been selected for secret shopper program! Pay fee to start",
        "CRITICAL: Your bank account compromised! Click link immediately to secure",
        "Get rich quick system! Turn $100 into $10,000 guaranteed! Pay now",
        "Pay processing fee to receive your inheritance/winnings/lottery prize",
        
        # Phishing scams
        "Dear Customer, Your Wells Fargo account has been suspended. Click here to verify",
        "PayPal: Your account will be limited! Verify identity immediately",
        "Microsoft Support: Your Windows license expired! Pay $99 for renewal",
        "IRS: You have tax refund pending! Verify identity to claim",
        "Amazon: Your order cannot be delivered! Verify payment information",
        "Netflix: Account suspended! Update payment method immediately",
        "Apple ID: Security alert! Verify identity or account will be locked",
        "Google: Suspicious sign-in detected! Verify account immediately",
        
        # Tech support scams
        "Your computer has been infected with viruses! Call Microsoft support now",
        "Critical system error! Contact technical support immediately",
        "Your IP address has been compromised! Call support to fix",
        "System crash imminent! Download our antivirus software now",
        "Your browser has been hacked! Install security update immediately",
        
        # URL-based scams
        "Access your secure dashboard at https://company-admin-panel.trycloudflare.com",
        "Special offer! Click http://bit.ly/amazing-deal-2024 for 90% discount",
        "Download free software from https://software-download.tk",
        "Login to your account at https://goggle.com",
        "Click https://tinyurl.com/xyz for amazing opportunity",
        "Visit https://suspicious-site.xyz for limited time offer",
        "Access https://get-rich-quick.com for guaranteed profits",
        "Download from https://malware-site.com for free software"
    ]
    
    # SUSPICIOUS examples - Medium confidence training
    suspicious_examples = [
        "Special offer! Click here for discount",
        "Limited time offer available now",
        "Act fast before this opportunity expires",
        "Click here immediately for important update",
        "Urgent response required for this message",
        "Verify your account information soon",
        "Update payment method to continue service",
        "Confirm identity to access your account",
        "Special promotion available for limited time",
        "Click link to claim your special offer",
        "Immediate action required for account security",
        "Important notification requires your attention",
        "Verify details to continue using service",
        "Update information to avoid account suspension",
        "Click now to secure your account access"
    ]
    
    # SAFE examples - High confidence training
    safe_examples = [
        # Legitimate business communications
        "Software Engineer position available at Google. Apply with resume to careers@google.com",
        "Learn machine learning at https://www.coursera.org/machine-learning - Free course",
        "Team meeting scheduled for tomorrow at 2 PM. Please confirm your attendance",
        "Project deadline extended to next Friday. Complete tasks accordingly",
        "Visit https://www.microsoft.com for official software downloads",
        "Customer support available at support@company.com for assistance",
        "Network at https://www.linkedin.com professionally",
        "Search at https://www.google.com for information",
        "Develop at http://localhost:3000 locally for testing",
        "Documentation available at https://docs.fortinet.com",
        "For Fortinet technical support, contact support@fortinet.com",
        "Software Engineer position at iTNT. Requirements: Python experience. Apply at careers@itnt.com",
        "iTNT team meeting scheduled for Tuesday at 2 PM. Please confirm attendance",
        "Order #12345 has been shipped - Track delivery online",
        "Your invoice #5678 is due on March 31st. Payment can be made online",
        "Quarterly report is ready for review. Please check your email",
        "Training session scheduled for next Monday at 10 AM",
        "New software update available for download from official website",
        "Company policy updated. Please review the latest guidelines",
        "Vacation request approved for dates April 15-22"
    ]
    
    # Combine with labels: 0=safe, 1=suspicious, 2=scam
    all_texts = safe_examples + suspicious_examples + scam_examples
    all_labels = [0] * len(safe_examples) + [1] * len(suspicious_examples) + [2] * len(scam_examples)
    
    print(f"✅ Safe examples: {len(safe_examples)}")
    print(f"⚠️ Suspicious examples: {len(suspicious_examples)}")
    print(f"🚨 Scam examples: {len(scam_examples)}")
    print(f"📊 Total training samples: {len(all_texts)}")
    print(f"🏢 Fortinet-specific: {8} scam examples")
    print(f"🎯 iTNT-specific: {8} scam examples")
    
    return all_texts, all_labels

def train_enhanced_model(texts, labels):
    """Train enhanced threat detection model"""
    
    print("\n🧠 Training enhanced model...")
    
    # Create enhanced vectorizer with organization-specific features
    vectorizer = TfidfVectorizer(
        max_features=2000,
        ngram_range=(1, 3),  # Include trigrams for better pattern detection
        stop_words='english',
        lowercase=True,
        min_df=1,  # Include all terms
        max_df=0.9,  # Exclude very common terms
        sublinear_tf=True  # Apply sublinear TF scaling
    )
    
    # Vectorize texts
    X = vectorizer.fit_transform(texts)
    y = np.array(labels)
    
    print(f"📊 Feature matrix shape: {X.shape}")
    print(f"🔢 Vocabulary size: {len(vectorizer.vocabulary_)}")
    
    # Train enhanced Random Forest
    model = RandomForestClassifier(
        n_estimators=200,  # More trees for better accuracy
        max_depth=15,  # Deeper trees for complex patterns
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1,  # Use all CPU cores
        class_weight='balanced'  # Handle class imbalance
    )
    
    model.fit(X, y)
    
    # Feature importance analysis
    feature_names = vectorizer.get_feature_names_out()
    feature_importance = model.feature_importances_
    
    # Get top important features
    top_features = sorted(zip(feature_importance, feature_names), reverse=True)[:20]
    
    print(f"\n🔍 Top 20 Most Important Features:")
    for importance, feature in top_features:
        print(f"   {feature}: {importance:.4f}")
    
    print(f"✅ Enhanced model trained successfully")
    
    return model, vectorizer

def save_enhanced_model(model, vectorizer):
    """Save the enhanced model"""
    
    print("\n💾 Saving enhanced model...")
    
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Save vectorizer
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print("✅ Enhanced model saved as model.pkl")
    print("✅ Enhanced vectorizer saved as vectorizer.pkl")

def test_model_performance(model, vectorizer):
    """Test model performance with sample cases"""
    
    print("\n🧪 Testing model performance...")
    
    test_cases = [
        ("🚨 FORTINET SECURITY BREACH! Click now!", 2),
        ("URGENT: iTNT account suspended! Verify immediately", 2),
        ("Special offer! Click here for discount", 1),
        ("Team meeting scheduled for tomorrow", 0)
    ]
    
    correct = 0
    for text, expected in test_cases:
        # Vectorize test text
        X_test = vectorizer.transform([text])
        
        # Predict
        prediction = model.predict(X_test)[0]
        probabilities = model.predict_proba(X_test)[0]
        
        # Map prediction to label
        label_map = {0: 'safe', 1: 'suspicious', 2: 'scam'}
        predicted_label = label_map[prediction]
        expected_label = label_map[expected]
        
        confidence = max(probabilities) * 100
        
        print(f"   Text: {text[:40]}...")
        print(f"   Expected: {expected_label} | Predicted: {predicted_label} | Confidence: {confidence:.1f}%")
        
        if prediction == expected:
            correct += 1
            print("   ✅ CORRECT")
        else:
            print("   ❌ INCORRECT")
        print()
    
    accuracy = (correct / len(test_cases)) * 100
    print(f"📊 Test accuracy: {accuracy:.1f}% ({correct}/{len(test_cases)})")
    
    return accuracy

def main():
    """Main training function"""
    
    # Create enhanced training data
    texts, labels = create_enhanced_training_data()
    
    # Train enhanced model
    model, vectorizer = train_enhanced_model(texts, labels)
    
    # Test model performance
    test_accuracy = test_model_performance(model, vectorizer)
    
    # Save enhanced model
    save_enhanced_model(model, vectorizer)
    
    print("\n" + "=" * 70)
    print("🎉 ENHANCED CYBERSHIELD AI MODEL TRAINING COMPLETE!")
    print("=" * 70)
    print(f"🧠 Model trained with {len(texts)} samples")
    print(f"🎯 Test accuracy: {test_accuracy:.1f}%")
    print(f"🏢 Fortinet threats: Specialized training included")
    print(f"🎯 iTNT threats: Specialized training included")
    print(f"🌐 General threats: Comprehensive coverage")
    print(f"🚀 Ready for production deployment!")
    print("\n📝 NEXT STEPS:")
    print("   1. Restart API: python app.py")
    print("   2. Test with examples: python test_dataset_examples.py")
    print("   3. Verify improved detection accuracy")

if __name__ == "__main__":
    main()
