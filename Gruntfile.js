
module.exports = function (grunt) {
  'use strict';

  require('load-grunt-tasks')(grunt);
  grunt.file.setBase('src/rer/pubblicazioni/browser');
  grunt.initConfig({
    requirejs: {
      'rer-pubblicazioni': {
        options: {
          baseUrl: `.`,
          generateSourceMaps: true,
          preserveLicenseComments: false,
          paths: {
            jquery: 'empty:',
          },
          wrapShim: true,
          name: `./static/rerpubblicazioni.js`,
          exclude: ['jquery'],
          out: `./static/rerpubblicazionibundle.js`,
          optimize: 'none',
        },
      },
    },
    uglify: {
      'rer-pubblicazioni': {
        options: {
          sourceMap: true,
          sourceMapName: `./static/rerpubblicazionibundle-compiled.js.map`,
          sourceMapIncludeSources: false,
        },
        files: {
          './static/rerpubblicazionibundle.js': ['./static/rerpubblicazionibundle.js'],
        },
      },
    },
  });

  grunt.registerTask('compile', ['requirejs', 'uglify']);

};
