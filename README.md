# Bulk Product Image Optimizer for BigCommerce

This extension automatically compresses and optimizes product images in a BigCommerce store to improve page speed and SEO. It integrates with the BigCommerce API, processes images using open-source tools, and replaces them with optimized versions.

## Tech Stack

### Frontend (User Dashboard)
- **Framework:** React.js
- **State Management:** Redux
- **UI Components:** Material-UI

### Backend (API & Image Processing)
- **Framework:** FastAPI
- **Image Processing:** Sharp.js (Node.js) or ImageMagick (Python)
- **Database:** PostgreSQL
- **Authentication:** OAuth2

### Storage & Deployment
- **Storage:** MinIO
- **Server:** Docker + Kubernetes
- **Cloud Hosting:** AWS, DigitalOcean, or self-hosted

## System Architecture

BigCommerce Store  →  App Dashboard  →  Image Processing API  →  Storage & CDN  →  Updated Images in Store

## Workflow

1. **Authentication & Setup**: The merchant installs the app from the BigCommerce App Marketplace and authenticates using OAuth2.
2. **Fetch Product Images**: Retrieves all product images via the BigCommerce API and saves the image URLs & metadata in the database.
3. **Image Optimization**: Downloads images, compresses them, converts to next-gen formats, and resizes based on store settings.
4. **Upload Optimized Images**: Stores optimized images in MinIO and replaces old images via the BigCommerce API.
5. **Dashboard & Logs**: Merchants see optimization stats and can revert changes if needed.
6. **Scheduled Optimization**: A cron job runs periodically to check for new images & optimize them automatically.

## Deployment Plan

| **Component**            | **Technology**          | **Deployment**            |
|--------------------------|------------------------|---------------------------|
| Frontend (Dashboard)     | React.js | Vercel / Netlify          |
| Backend (API)            | FastAPI (Python)       | Docker + Kubernetes (AWS / GCP) |
| Image Processing         | Sharp.js / ImageMagick | Runs inside backend API   |
| Storage                 | MinIO (S3 alternative)  | Self-hosted / Cloud S3    |
| Database                | PostgreSQL             | Hosted on DigitalOcean / AWS RDS |
| Authentication          | OAuth2 (BigCommerce)   | Handled via backend API   |

## Future Enhancements

- Add AI-based image enhancement using OpenCV
- Allow merchants to preview optimization before applying
- Provide detailed analytics on storage savings

---

For more information on Create React App, visit the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
