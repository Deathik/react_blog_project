var path = require("path");
var webpack = require("webpack");

module.exports = {
    entry: {
        main: './react_blog/src/index.js'
    },

    output: {
        path: path.resolve(__dirname, 'react_blog/static/react/'),
        filename: "[name].bundle.js"
    },
    // plugins: [
    //     new webpack.DefinePlugin({
    //         'process.env': {
    //             'NODE_ENV': JSON.stringify('production')
    //         }
    //     }),
    //     new webpack.optimize.UglifyJsPlugin({
    //         comments: false,
    //         compress: {
    //             unused: true,
    //             dead_code: true,
    //             warnings: false,
    //         }
    //     })
    // ],
    module: {
        loaders:[
            {
                test: /\.js$/,
                exclude: /node_modules/, 
                loader: 'babel-loader',
                options: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
}