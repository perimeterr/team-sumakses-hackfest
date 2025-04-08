import styles from './Button.module.css';
import { FaArrowRight } from 'react-icons/fa';

function ShopButton() {

    return(
        <button className={styles.shopButton}>
            <span className={styles.shopText}>SHOP UPCYCLABLES <FaArrowRight /></span>
        </button>
    );
}

export default ShopButton