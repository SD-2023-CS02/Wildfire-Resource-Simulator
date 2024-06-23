## Possible Webapp Issues

* Google Maps Marker Deprecation
    * This component was deprecated by Google around February of 2024. 
    * If for some reason, problems occur with the icon, it is suggested to replace `<Markers ...>` with [AdvancedMarkers](https://developers.google.com/maps/documentation/javascript/reference/advanced-markers)

* NPM Package Updating
    * It is possible that npm packages update and that require them to be update to reduce any risk of errors.    
    * A great example for this is the `serve` development dependency to serve the webapp locally as if it were "Production".
    * Typically packages will inform you, but if they don't it's best to lookup if the package has updated
    * For example, here is [serve](https://www.npmjs.com/package/serve) as an example. As of `05-06-2024`, serve's version was `v14.2.3`.
    * You can also run `npm outdated` and if there are any updates to be made then run `npm update`.