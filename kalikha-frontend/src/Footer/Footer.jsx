import styles from './Footer.module.css';
import { FaFacebookF, FaInstagram, FaLinkedinIn, FaTwitter } from 'react-icons/fa';
import logo from '../assets/desktop header logo.png';

function Footer() {
    return (
        <footer className={styles.footer}>
            <div className={styles.footerContent}>
                <div className={styles.logoSection}>
                    <img src={logo} alt="KaLikha Logo" className={styles.logo} />
                </div>
                <div className={styles.linksSection}>
                    <a href="#" onClick={(e) => e.preventDefault()}>Help</a>
                    <a href="#" onClick={(e) => e.preventDefault()}>Contact</a>
                    <a href="#" onClick={(e) => e.preventDefault()}>About</a>
                </div>
                <div className={styles.socialSection}>
                    <a href="#" onClick={(e) => e.preventDefault()} aria-label="Twitter"><FaTwitter /></a>
                    <a href="#" onClick={(e) => e.preventDefault()} aria-label="Instagram"><FaInstagram /></a>
                    <a href="#" onClick={(e) => e.preventDefault()} aria-label="LinkedIn"><FaLinkedinIn /></a>
                    <a href="#" onClick={(e) => e.preventDefault()} aria-label="Facebook"><FaFacebookF /></a>
                </div>
            </div>
            <div className={styles.horizontalBar}></div>
            <div className={styles.footerBottom}>
                <p>Sa KaLikha, sama-sama tayong lilikha para sa kinabukasan. <span className={styles.greenHeart}>💚</span></p>
                <p>&copy; {new Date().getFullYear()} KaLikha</p>
            </div>
        </footer>
    );
}

export default Footer;