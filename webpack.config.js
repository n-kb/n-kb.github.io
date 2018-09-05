var path = require('path')
var webpack = require('webpack')
const PrerenderSPAPlugin = require('prerender-spa-plugin')
const Renderer = PrerenderSPAPlugin.PuppeteerRenderer
var UglifyJSPlugin = require('uglifyjs-webpack-plugin');

const file = require('fs')
var parse = require('csv-parse/lib/sync')

// Reading file
let readFile = (filename) => {
    return new Promise(function(resolve, reject) {
        file.readFile(filename, 'utf8', function(err, data) {
            if (err) {
                reject(err)
            } else {
                var routes = ['/']
                csv = parse(data, {
                    delimiter: ","
                })
                csv.forEach(function(row) {
                    if (row[1] != 'url' && row[4] == '0') {
                        routes.push("/" + row[1])
                    }
                })
                resolve(routes)
            }
        });
    });
}

module.exports = readFile('./_public/assets/articles.csv')
    .then(function(all_routes) {
        return {
            entry: './_src/main.js',
            output: {
                path: path.resolve(__dirname, './_dist'),
                publicPath: '/_dist/',
                filename: 'build.js'
            },
            module: {
                rules: [{
                        test: /\.css$/,
                        use: [
                            'vue-style-loader',
                            'css-loader'
                        ],
                    },
                    {
                        test: /\.scss$/,
                        use: [
                            'vue-style-loader',
                            'css-loader',
                            'sass-loader'
                        ],
                    },
                    {
                        test: /\.sass$/,
                        use: [
                            'vue-style-loader',
                            'css-loader',
                            'sass-loader?indentedSyntax'
                        ],
                    },
                    {
                        test: /\.vue$/,
                        loader: 'vue-loader',
                        options: {
                            loaders: {
                                // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
                                // the "scss" and "sass" values for the lang attribute to the right configs here.
                                // other preprocessors should work out of the box, no loader config like this necessary.
                                'scss': [
                                    'vue-style-loader',
                                    'css-loader',
                                    'sass-loader'
                                ],
                                'sass': [
                                    'vue-style-loader',
                                    'css-loader',
                                    'sass-loader?indentedSyntax'
                                ]
                            }
                            // other vue-loader options go here
                        }
                    },
                    {
                        test: /\.js$/,
                        loader: 'babel-loader',
                        exclude: /node_modules/
                    },
                    {
                        test: /\.(png|jpg|gif|svg)$/,
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]?[hash]'
                        }
                    }
                ]
            },
            resolve: {
                alias: {
                    'vue$': 'vue/dist/vue.esm.js'
                },
                extensions: ['*', '.js', '.vue', '.json']
            },
            devServer: {
                historyApiFallback: true,
                noInfo: true,
                overlay: true
            },
            performance: {
                hints: "warning"
            },
            devtool: '#source-map',
            plugins: [
                new PrerenderSPAPlugin({
                    // Required - The path to the webpack-outputted app to prerender.
                    staticDir: path.join(__dirname, './'),
                    indexPath: path.resolve('./index.html'),
                    // Required - Routes to render.
                    routes: all_routes,
                    postProcessHtml: function(renderedRoute) {
                        // index.html needs no rendering
                        if (renderedRoute.route == "/") {
                            renderedRoute.html = `
                              <!DOCTYPE html>
                              <html lang="en">
                                <head>
                                  <meta charset="utf-8">
                                  <link rel="icon" href="favicon.ico">
                                  <meta itemprop="name" content="Nicolas Kayser-Bril">
                                  <meta property="og:title" content="Nicolas Kayser-Bril">
                                  <meta name="twitter:title" content="Nicolas Kayser-Bril">
                                  <meta name="description" content="Data-driven journalist, author, trainer, public speaker and project manager."/>
                                  <meta itemprop="description" content="Data-driven journalist, author, trainer, public speaker and project manager.">
                                  <meta property="og:description" content="Data-driven journalist, author, trainer, public speaker and project manager.">
                                  <meta name="twitter:description" content="Data-driven journalist, author, trainer, public speaker and project manager.">
                                  <meta itemprop="image" content="https://blog.nkb.fr/_public/images/share.png">
                                  <meta property="og:image" content="https://blog.nkb.fr/_public/images/share.png">
                                  <meta name="twitter:image" content="https://blog.nkb.fr/_public/images/share.png">
                                  <meta name="author" content="Nicolas Kayser-Bril" />
                                  <meta name="twitter:card" content="summary_large_image">
                                  <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                  <title>Nicolas Kayser-Bril, datajournalist</title>
                                </head>
                                <body>
                                  <div id="app"></div>
                                  <script src="./_dist/build.js"></script>

                                  <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js"></script>
                                </body>
                              </html>
                              `
                        } else {
                            function replaceAll(str, find, replace) {
                                return str.replace(new RegExp(find, 'g'), replace);
                            }
                            // fixes the URL of images
                            renderedRoute.html = replaceAll(renderedRoute.html, "\./_public/images/", "../_public/images/");
                            renderedRoute.html = renderedRoute.html.replace("./_dist/build.js", "../_dist/build.js");
                            renderedRoute.html = renderedRoute.html.replace("favicon.ico", "../favicon.ico");
                        }
                        return renderedRoute
                    },
                    renderer: new Renderer({
                        renderAfterTime: 10000,
                        //renderAfterElementExists: "#isLoaded",
                        maxConcurrentRoutes: 4,
                        headless:true
                    })
                }),
                new webpack.DefinePlugin({
                    'process.env': {
                        NODE_ENV: '"production"'
                    }
                }),
                new UglifyJSPlugin({
                  sourceMap: true
                }),
                new webpack.LoaderOptionsPlugin({
                    minimize: true
                })
            ]
        }
    })