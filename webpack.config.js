const path = require('path');  
const HtmlWebpackPlugin = require('html-webpack-plugin');  

module.exports = {  
  entry: './src/index.js',  // Your entry point  
  output: {  
    path: path.resolve(__dirname, 'dist'), // Output directory  
    filename: 'bundle.js',  // Name of the output bundle  
    clean: true,  // Cleans the output directory before each build  
  },  
  module: {  
    rules: [  
      {  
        test: /\.(js|jsx)$/, // Files to be transformed  
        exclude: /node_modules/,  // Don't transpile dependencies  
        use: {  
          loader: 'babel-loader',  
          options: {  
            presets: ['@babel/preset-env', '@babel/preset-react'],  
          },  
        },  
      },  
    ],  
  },  
  resolve: {  
    extensions: ['.js', '.jsx'], // Resolve these extensions  
  },  
  devServer: {  
    static: './dist',  
    historyApiFallback: true, // For SPA navigation with React Router  
  },  
  plugins: [  
    new HtmlWebpackPlugin({  
      template: './src/index.html', // Template for the HTML file  
      filename: 'index.html', // Output HTML file  
    }),  
  ],  
  mode: 'development', // Use 'production' for optimized builds  
};