Worthless Pixels NFT Dashboard

Welcome to the Worthless Pixels NFT Dashboard, the quintessential tool for managing and displaying metadata for Solana NFTs. This dashboard is an amalgamation of elegance and functionality, designed to provide a seamless experience for NFT collections management.


Features

Dynamic Content Loading: Utilize HTMX to load and render NFT metadata dynamically, without the need for page reloads.
Live Search & Filtering: Effortlessly search and filter through your NFT collection with real-time updates.
Data Presentation: View decrypted metadata in a user-friendly format, including attributes like guid, class, week, and lucky_code.
Responsive Design: A dashboard that looks good on any device, ensuring you can manage your collection anytime, anywhere.
Secure Backend: Built with FastAPI, MongoDB, and state-of-the-art encryption, your data's integrity and security are paramount.


Project Structure

main.py: The heart of the FastAPI backend, handling all routing and server-side logic.
models.py: Pydantic models that define the structure of the NFT metadata.
templates/: Jinja2 templates that render the frontend, ensuring a smooth and reactive user experience.
