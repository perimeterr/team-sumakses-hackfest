import styles from './Listings.module.css';
import placeholderImage from '../assets/pexels-cottonbro-7191423 1.png';
import { Link } from 'react-router-dom';
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { faHeart as solidHeart } from '@fortawesome/free-solid-svg-icons';
import { faHeart as regularHeart } from '@fortawesome/free-regular-svg-icons';

function Listings(props) {
    const [searchTerm, setSearchTerm] = useState('');
    const [likedItems, setLikedItems] = useState({});

    const toggleLike = (id) => {
        setLikedItems((prevLikedItems) => ({
            ...prevLikedItems,
            [id]: !prevLikedItems[id],
        }));
    };

    const items = props.items || [
        { id: 1, name: 'Plastic Bottles', quantity: 9999, provider: 'Provider 1', image: placeholderImage },
        { id: 2, name: 'Plastic Bottles', quantity: 9999, provider: 'Provider 2', image: placeholderImage },
        { id: 3, name: 'Plastic Bottles', quantity: 9999, provider: 'Provider 3', image: placeholderImage },
        { id: 4, name: 'Plastic Bottles', quantity: 9999, provider: 'Provider 4', image: placeholderImage },
        { id: 5, name: 'Plastic Bottles', quantity: 9999, provider: 'Provider 5', image: placeholderImage },
    ];

    const filteredItems = items.filter(item => item.name.toLowerCase().includes(searchTerm.toLowerCase()));

    return (
        <div className={styles.listingsContainer}>
            <div className={styles.headerContainer}>
                <h1 className={styles.listingsHeader}>Listings</h1>
                <div className={styles.searchContainer}>
                    <FontAwesomeIcon icon={faSearch} className={styles.searchIconInside} />
                    <input
                        type="text"
                        placeholder="Search for upcyclables"
                        className={styles.searchBarWithIcon}
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>
            </div>
            <hr className={styles.horizontalBar} />
            <div className={styles.itemsGrid}>
                {filteredItems.map(item => (
                    <Link 
                        to={`/listings/${item.id}`} 
                        key={item.id} 
                        className={styles.itemCard}
                        onClick={(e) => {
                            if (e.target.closest(`.${styles.heartButton}`)) {
                                e.preventDefault();
                                return;
                            }
                            window.scrollTo({ top: 0 });
                        }}
                    >
                        <img src={item.image} alt={item.name} className={styles.itemImage} />
                        <h2 className={styles.itemName}>{item.name}</h2>
                        <p className={styles.itemQuantity}>
                            Quantity: {item.quantity}
                            <span className={styles.heartButtonWrapper}>
                                <button 
                                    className={styles.heartButton} 
                                    onClick={(e) => {
                                        e.preventDefault();
                                        toggleLike(item.id);
                                    }}
                                >
                                    <FontAwesomeIcon 
                                        icon={likedItems[item.id] ? solidHeart : regularHeart} 
                                        className={`${styles.heartIcon} ${likedItems[item.id] ? styles.liked : ''}`} 
                                    />
                                </button>
                            </span>
                        </p>
                        <p className={styles.itemProvider}>Provider: {item.provider}</p>
                    </Link>
                ))}
            </div>
        </div>
    );
}

export default Listings;