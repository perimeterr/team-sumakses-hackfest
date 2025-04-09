import styles from './CreateAccount.module.css';
import backdropImage from '../assets/Create account image backdrop.png';
import { FaArrowRight } from 'react-icons/fa';

function CreateAccount() {
    return (
        <div className={styles.createAccountContainer}>
            <div className={styles.imageSection}>
                <img src={backdropImage} alt="Create Account Backdrop" className={styles.backdropImage} />
            </div>
            <div className={styles.formSection}>
                <h2 className={styles.createAccount}>Create Account</h2>
                <p>I am...</p>
                <form>
                    <label>
                        <input type="radio" name="userType" value="provider" /> a Resource Provider
                    </label>
                    <label>
                        <input type="radio" name="userType" value="upcycler" /> an Upcycler
                    </label>
                    <button className={styles.splitButton} type="submit">
                        <span className={styles.textPart}>Next</span>
                        <span className={styles.arrowPart}><FaArrowRight /></span>
                    </button>
                </form>
            </div>
        </div>
    );
}

export default CreateAccount;