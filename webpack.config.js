var path = require('path')
var webpack = require('webpack')
const PrerenderSPAPlugin = require('prerender-spa-plugin')
const Renderer = PrerenderSPAPlugin.PuppeteerRenderer

const file = require('fs')
var parse = require('csv-parse/lib/sync')

// Reading file
let readFile =(filename)=>{
  return new Promise(function(resolve, reject){
    file.readFile(filename, 'utf8', function(err, data){
      if(err){
        reject(err)
      }else{
        var routes = ['/']
        csv = parse(data, {delimiter:","})
        csv.forEach(function(row){
          if (row[1] != 'url'){ routes.push("/" + row[1]) }
        })
        resolve(routes)
      }
    });
  });
}

var all_routes2 = ["/", "pourquoi-les-femmes-sont-plus-petites"]

module.exports = readFile('./public/assets/articles.csv')
.then(function(all_routes){
  return {
    entry: './src/main.js',
    output: {
      path: path.resolve(__dirname, './dist'),
      publicPath: '/dist/',
      filename: 'build.js'
    },
    module: {
      rules: [
      {
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
        test: /\.(png|jpg|gif|svg|csv)$/,
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
      hints: false
    },
    devtool: '#eval-source-map',
    plugins: [
    new PrerenderSPAPlugin({
      // Required - The path to the webpack-outputted app to prerender.
      staticDir: path.join(__dirname, './'),
      indexPath: path.resolve('./index.html'),
      // Required - Routes to render.
      routes: all_routes,
      postProcessHtml: function (renderedRoute) {
        // index.html needs no rendering
        if (renderedRoute.route == "/") {
          renderedRoute.html = `
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="icon" href="favicon.ico">
    <meta name="author" content="Nicolas Kayser-Bril" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nicolas Kayser-Bril, datajournalist</title>
  </head>
  <body>
    <div id="app"></div>
    <script src="./dist/build.js"></script>
    <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js"></script>
  </body>
</html>
          `
        } else {
          // fixes the URL of images
          renderedRoute.html = renderedRoute.html.replace("./public/images/", "../public/images/");
          renderedRoute.html = renderedRoute.html.replace("./dist/build.js", "../dist/build.js");
        }
        return renderedRoute
      }
    })
    ]
  }

  if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
    ])
}
})