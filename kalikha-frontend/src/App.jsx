import Header from './Header/Header.jsx';
import Footer from './Footer/Footer.jsx';
import CreateAccount from './CreateAccount/CreateAccount.jsx';
import styles from './App.module.css';
import heroImage from './assets/Hero v2 - Desktop.png';
import ShopButton from './Button/ShopButton.jsx';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Listings from './Listings/Listings.jsx';
import DetailedItem from './DetailedItem/DetailedItem.jsx';

function App() {
    return (
        <Router>
            <div className={styles.appContainer}>
                <Header />
                <main className={styles.mainContent}>
                    <Routes>
                        <Route path="/" element={
                            <>
                                <section className={styles.heroSection}>
                                    <img src={heroImage} alt="Hero" className={styles.heroImage} />
                                </section>
                                <ShopButton />
                                <CreateAccount />
                            </>
                        } />
                        <Route path="/listings" element={<Listings />} />
                        <Route path="/listings/:id" element={<DetailedItem />} />
                    </Routes>
                </main>
                <Footer />
            </div>
        </Router>
    );
}

export default App;