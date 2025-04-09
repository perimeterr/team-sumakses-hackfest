import styles from './Button.module.css';
import { FaArrowRight } from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';


function ShopButton() {
    const navigate = useNavigate();

    const handleClick = () => {
        window.scrollTo({ top: 0});
        navigate('/listings');
    };

    return (
        <button onClick={handleClick} className={styles.shopButton}>
            <span className={styles.shopText}>
                SHOP UPCYCLABLES <FaArrowRight />
            </span>
        </button>
    );
}

export default ShopButton