import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { LoremIpsum } from 'lorem-ipsum';
import styles from './DetailedItem.module.css';
import image1 from '../assets/pexels-cottonbro-7191423 1.png';

import { FaArrowRight, FaArrowLeft, FaRegHeart, FaHeart } from 'react-icons/fa';

const DetailedItem = (props) => {
    const { id } = useParams();
    const lorem = new LoremIpsum();
    
    const description = `
        <div class="crateAnnouncement">
            <p>
                We're giving away 50 crates of clean, empty glass bottles – ideal for upcycling, crafting, DIY projects, or creative reuse.
                Whether you're making vases, candles, storage jars, or something totally unique, these bottles are ready for a second life.
            </p>
            <ul>
                <li>Washed and crate-packed</li>
                <li>Great for artists, crafters, small businesses, or community projects</li>
                <li>First come, first served – pickup only</li>
            </ul>
            <p>
                Let's keep them out of the landfill and turn them into something beautiful. Interested? Reach out to claim your crates!
            </p>
        </div>
    `;

    const items = props.items || [
        { id: 1, name: 'Item 1', quantity: 9999, description: description, provider: 'Bob Baker', images: [image1, image1, image1, image1] },
        { id: 2, name: 'Item 2', quantity: 9999, description: description, provider: 'Bob Baker', images: [image1, image1, image1, image1] },
        { id: 3, name: 'Item 3', quantity: 9999, description: description, provider: 'Bob Baker', images: [image1, image1, image1, image1] },
    ];

    const item = items.find(item => item.id === parseInt(id));

    const [currentImageIndex, setCurrentImageIndex] = useState(0);
    const [liked, setLiked] = useState(false);
    const imagesToShow = 3; // Number of images to display at a time

    if (!item) {
        return <div className={styles.error}>Item not found</div>;
    }

    const handleNextImage = () => {
        setCurrentImageIndex((prevIndex) => (prevIndex + 1) % item.images.length);
    };

    const handlePrevImage = () => {
        setCurrentImageIndex((prevIndex) => (prevIndex - 1 + item.images.length) % item.images.length);
    };

    const toggleLike = () => {
        setLiked(!liked);
    };

    const visibleImages = item.images.slice(currentImageIndex, currentImageIndex + imagesToShow).concat(
        item.images.slice(0, Math.max(0, currentImageIndex + imagesToShow - item.images.length))
    );

    return (
        <div className={styles.detailedItemContainer}>
            <div className={styles.imageCarousel}>
                <button className={styles.arrowButton} onClick={handlePrevImage}><FaArrowLeft /></button>
                <div className={styles.imageWrapper}>
                    {visibleImages.map((image, index) => (
                        <img
                            key={index}
                            src={image}
                            alt={`${item.name} ${index + 1}`}
                            className={styles.itemImage}
                        />
                    ))}
                </div>
                <button className={styles.arrowButton} onClick={handleNextImage}><FaArrowRight /></button>
            </div>
            <div className={styles.textContainer}>
                <div className={styles.headerRow}>
                    <div className={styles.itemContainer}>
                        <h1 className={styles.itemName}>{item.name}</h1>
                        <p className={styles.itemQuantity}>Quantity: {item.quantity}</p>
                    </div>
                    <div className={styles.cardSection}>
                        <div className={styles.cardContainer}>
                            <div className={styles.heartButton}>
                                {liked ? (
                                    <FaHeart 
                                        className={`${styles.heartIcon} ${styles.liked}`} 
                                        onClick={toggleLike} 
                                    />
                                ) : (
                                    <FaRegHeart 
                                        className={styles.heartIcon} 
                                        onClick={toggleLike} 
                                    />
                                )}
                            </div>
                            <div className={styles.providerInfoContainer}>
                                <div className={styles.profilePicture}>
                                    <img src={image1} alt={`${item.provider}'s profile`} />
                                </div>
                                <p className={styles.itemProvider}>{item.provider}</p>
                            </div>
                            <p className={styles.providerContact}>+1 234 567 890</p>
                            <p className={styles.providerEmail}>email@example.com</p>
                            <button className={styles.chatButton}>CHAT</button>
                        </div>
                    </div>
                </div>
                <h2>Description:</h2>
                <div 
                    className={styles.itemDescription}
                    dangerouslySetInnerHTML={{ __html: item.description }}
                />
            </div>
        </div>
    );
};

export default DetailedItem;