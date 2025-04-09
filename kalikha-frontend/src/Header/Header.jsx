import styles from './Header.module.css';
import logo from '../assets/desktop header logo.png';
import { Link } from 'react-router-dom';

function Header() {
    return (
        <header className={styles.header}>
            <Link to="/">
                <img src={logo} alt="KaLikha Logo" className={styles.logo} />
            </Link>
            <nav>
                <ul className={styles.navList}>
                    <li><Link to="/listings">Listings</Link></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Sign In/Sign Up</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;