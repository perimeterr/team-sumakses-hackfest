import Header from './Header/Header.jsx';
import Footer from './Footer/Footer.jsx';
import CreateAccount from './CreateAccount/CreateAccount.jsx';
import styles from './App.module.css';
import heroImage from './assets/Hero v2 - Desktop.png';
import ShopButton from './Button/ShopButton.jsx';

function App() {
    return (
        <div className={styles.appContainer}>
            <Header />
            <main className={styles.mainContent}>
                <section className={styles.heroSection}>
                    <img src={heroImage} alt="Hero" className={styles.heroImage} />
                </section>
                <ShopButton />
                <CreateAccount />
            </main>
            <Footer />
        </div>
    );
}

export default App;