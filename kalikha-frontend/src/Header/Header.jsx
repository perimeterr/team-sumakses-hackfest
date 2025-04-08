import styles from './Header.module.css';
import logo from '../assets/desktop header logo.png';

function Header() {
    return (
        <header className={styles.header}>
            <a href="#">
                <img src={logo} alt="KaLikha Logo" className={styles.logo} />
            </a>
            <nav>
                <ul className={styles.navList}>
                    <li><a href="#">Listings</a></li>
                    <li><a href="#">Sign In/Sign Up</a></li>
                    <li><a href="#">About</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;