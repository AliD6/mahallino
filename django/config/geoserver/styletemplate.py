
def __colorMap_colors(n):
    if n == 6:
        return "#06c888", "#1ace16", "#f3ff27", "#f18b36", "#ff4913", "#8c0101"
    if n == 7:
        return "#06c888", "#1ace16", "#f3ff27", "#f18b36", "#ff4913", "#d40000", "#863688"

    return None


def raster(**kwargs):
    name = kwargs.get('name', 'raster_layer')
    title = kwargs.get('title', 'Opaque Raster')
    opacity = kwargs.get('opacity', 0.8)
    colorMap_type = kwargs.get('colorMap_type', 'intervals')
    colors = kwargs.get('colors')
    quantities = kwargs.get('quantities')

    if quantities:
        if colors is None:
            colors = __colorMap_colors(len(quantities))

        assert len(colors) == len(quantities)

    template = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld\n'
        'http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">\n'
        '<UserLayer>'
            f'<Name>{name}</Name>'
            '<UserStyle>'
                '<Name>raster</Name>'
                f'<Title>{title}</Title>'
                '<Abstract>A sample style for rasters</Abstract>'
                '<FeatureTypeStyle>'
                    '<FeatureTypeName>Feature</FeatureTypeName>'
                        '<Rule>'
                            '<RasterSymbolizer>'
    )
    if quantities:
        template += (
                                f'<ColorMap type="{colorMap_type}">'
        )
    
        for c, q in zip(colors, quantities):
            template += (
                                    f'<ColorMapEntry color="{c}" quantity="{q}" opacity="{opacity}" />'
            )
        template += (
                                '</ColorMap>'
        )
    if not quantities:
        template += (
                            f'<Opacity>{opacity}</Opacity>'
        )
    template += (
                            '</RasterSymbolizer>'
                        '</Rule>'
                '</FeatureTypeStyle>'
            '</UserStyle>'
        '</UserLayer>'
        '</StyledLayerDescriptor>'
    )

    return template


def point(**kwargs):
    Name = kwargs.get('Name', 'Name')
    Title = kwargs.get('Title', 'Title')
    MinScaleDenominator = kwargs.get('MinScaleDenominator')
    MaxScaleDenominator = kwargs.get('MaxScaleDenominator')
    Filter = kwargs.get('Filter')
    Filter_PropertyName = kwargs.get('Filter_PropertyName')
    Filter_Literal = kwargs.get('Filter_Literal')
    Mark_fill = kwargs.get('Mark_fill')
    Mark_fill_opacity = kwargs.get('Mark_fill-opacity')
    Mark_stroke = kwargs.get('Mark_stroke')
    Mark_stroke_witdth = kwargs.get('Mark_stroke-width')
    Size = kwargs.get('Mark_Size')
    Rotation = kwargs.get('Mark_Rotation')
    Opacity = kwargs.get('Mark_Opacity')
    Mark_WellKnownName = kwargs.get('Mark_WellKnownName')
    Label_PropertyName = kwargs.get('Label_PropertyName', 'label')
    Label_fill = kwargs.get('Label_fill')
    Label_fill_opacity = kwargs.get('Label_fill-opacity')
    Label_stroke = kwargs.get('Label_stroke')
    Label_stroke_witdth = kwargs.get('Label_stroke-witdth')
    Label_font_family = kwargs.get('Label_font-family')
    Label_font_size = kwargs.get('Label_font-size')
    Label_font_style = kwargs.get('Label_font-style')
    Label_font_weight = kwargs.get('Label_font-weight')
    Label_AnchorPointX = kwargs.get('Label_AnchorPointX')
    Label_AnchorPointY = kwargs.get('Label_AnchorPointY')
    Label_DisplacementX = kwargs.get('Label_DisplacementX')
    Label_DisplacementY = kwargs.get('Label_DisplacementY')
    Label_Rotation = kwargs.get('Label_Rotation')
    ExternalGraphic_href = kwargs.get('ExternalGraphic_href')
    ExternalGraphic_Format = kwargs.get('ExternalGraphic_Format')

    template = (
        '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        '<StyledLayerDescriptor version="1.0.0"\n'
            'xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"\n'
            'xmlns="http://www.opengis.net/sld"\n'
            'xmlns:ogc="http://www.opengis.net/ogc"\n'
            'xmlns:xlink="http://www.w3.org/1999/xlink"\n'
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
            '<NamedLayer>'
                '<UserStyle>'
                    '<FeatureTypeStyle>'
                        '<Rule>'
                            f'<Name>{Name}</Name>'
                            f'<Title>{Title}</Title>'
    )
    if MinScaleDenominator:
        template +=(        f'<MinScaleDenominator>{MinScaleDenominator}</MinScaleDenominator>')
    if MaxScaleDenominator:
        template +=(        f'<MaxScaleDenominator>{MaxScaleDenominator}</MaxScaleDenominator>')
    if Filter and Filter_PropertyName and Filter_Literal:
        template +=(
                            '<ogc:Filter>'
                                f'<ogc:{Filter}>'
                                    f'<ogc:PropertyName>{Filter_PropertyName}</ogc:PropertyName>'
                                    f'<ogc:Literal>{Filter_Literal}</ogc:Literal>'
                                f'</ogc:{Filter}>'
                            '</ogc:Filter>'
        )
    template +=(
                            '<PointSymbolizer>'
                                '<Graphic>'
    ) 
    if Mark_WellKnownName and not ExternalGraphic_href:
        template +=(
                                    '<Mark>'
                                        f'<WellKnownName>{Mark_WellKnownName}</WellKnownName>'
        )
        if Mark_fill or Mark_fill_opacity:
            template +=(                '<Fill>')
            if Mark_fill:
                template +=(                f'<CssParameter name="fill">{Mark_fill}</CssParameter>')
            if Mark_fill_opacity:
                template +=(                f'<CssParameter name="fill-opacity">{Mark_fill_opacity}</CssParameter>')
            template +=(                '</Fill>')
        if Mark_stroke or Mark_stroke_witdth:
            template +=(                '<Stroke>')
            if Mark_stroke:
                template +=(                f'<CssParameter name="stroke">{Mark_stroke}</CssParameter>')
            if Mark_stroke_witdth:
                template +=(                f'<CssParameter name="stroke-width">{Mark_stroke_witdth}</CssParameter>')
            template +=(                '</Stroke>')
        template +=(                '</Mark>')
    else:
        template +=(                '<ExternalGraphic>'
                                        f'<OnlineResource xlink:type="simple" xlink:href="{ExternalGraphic_href}" />'
                                        f'<Format>{ExternalGraphic_Format}</Format>'
                                    '</ExternalGraphic>'
        )
    if Size:
        template +=(                f'<Size>{Size}</Size>')
    if Opacity:
        template +=(                f'<Opacity>{Opacity}</Opacity>')
    if Rotation:
        template +=(                f'<Rotation>{Rotation}</Rotation>')
    template +=(
                                '</Graphic>'
                            '</PointSymbolizer>'
    )
    if Label_PropertyName:
        template +=(
                            '<TextSymbolizer>'
                                '<Label>'
                                    f'<ogc:PropertyName>{Label_PropertyName}</ogc:PropertyName>'
                                '</Label>'
        )
        #  '<Halo>'
        #  '    <Radius>3</Radius>'
        #  '    <Fill>'
        #  '        <CssParameter name="fill">#FFFFFF</CssParameter>'
        #  '    </Fill>'
        #  '</Halo>'
        if Label_font_family or Label_font_size or Label_font_style or Label_font_weight:
            template +=(        '<Font>')
            if Label_font_family:
                template +=(        f'<CssParameter name="font-family">{Label_font_family}</CssParameter>')
            if Label_font_size:
                template +=(        f'<CssParameter name="font-size">{Label_font_size}</CssParameter>')
            if Label_font_style:
                template +=(        f'<CssParameter name="font-style">{Label_font_style}</CssParameter>')
            if Label_font_weight:
                template +=(        f'<CssParameter name="font-weight">{Label_font_weight}</CssParameter>')
            template +=(        '</Font>')
        if Label_AnchorPointX or Label_AnchorPointY or Label_DisplacementX or Label_DisplacementY or Label_Rotation:
            template +=(
                                '<LabelPlacement>'
                                    '<PointPlacement>'
            )
            if Label_AnchorPointX or Label_AnchorPointY:
                template +=(
                                        '<AnchorPoint>'
                                            f'<AnchorPointX>{Label_AnchorPointX}</AnchorPointX>'
                                            f'<AnchorPointY>{Label_AnchorPointY}</AnchorPointY>'
                                        '</AnchorPoint>'
                )
            if Label_DisplacementX or Label_DisplacementY:
                template +=(
                                        '<Displacement>'
                                            f'<DisplacementX>{Label_DisplacementX}</DisplacementX>'
                                            f'<DisplacementY>{Label_DisplacementY}</DisplacementY>'
                                        '</Displacement>'
                )
            if Label_Rotation:
                template +=(            f'<Rotation>{Label_Rotation}</Rotation>')
            template +=(
                                    '</PointPlacement>'
                                '</LabelPlacement>'
            )
        if Label_fill or Label_fill_opacity:
            template +=(        '<Fill>')
            if Label_fill:
                template +=(        f'<CssParameter name="fill">{Label_fill}</CssParameter>')
            if Label_fill_opacity:
                template +=(        f'<CssParameter name="fill-opacity">{Label_fill_opacity}</CssParameter>')
            template +=(        '</Fill>')
        if Label_stroke or Label_stroke_witdth:
            template +=(        '<Stroke>')
            if Label_stroke:
                template +=(        f'<CssParameter name="stroke">{Label_stroke}</CssParameter>')
            if Label_stroke_witdth:
                template +=(        f'<CssParameter name="stroke-width">{Label_stroke_witdth}</CssParameter>')
            template +=(        '</Stroke>')
        # '<VendorOption name="autoWrap">60</VendorOption>'
        # '<VendorOption name="maxDisplacement">150</VendorOption>'
        template +=(        '</TextSymbolizer>')
    template +=(
                        '</Rule>'
                    '</FeatureTypeStyle>'
                '</UserStyle>'
            '</NamedLayer>'
        '</StyledLayerDescriptor>'
    )
    return template


def polygon(**kwargs):
    Name = kwargs.get('Name', 'Name')
    Title = kwargs.get('Title', 'Title')
    MinScaleDenominator = kwargs.get('MinScaleDenominator')
    MaxScaleDenominator = kwargs.get('MaxScaleDenominator')
    Filter = kwargs.get('Filter')
    Filter_PropertyName = kwargs.get('Filter_PropertyName')
    Filter_Literal = kwargs.get('Filter_Literal')
    Mark_fill = kwargs.get('Mark_fill')
    Mark_fill_opacity = kwargs.get('Mark_fill-opacity')
    Mark_stroke = kwargs.get('Mark_stroke')
    Mark_stroke_witdth = kwargs.get('Mark_stroke-witdth')
    Size = kwargs.get('Mark_Size')
    Rotation = kwargs.get('Mark_Rotation')
    Opacity = kwargs.get('Mark_Opacity')
    Mark_WellKnownName = kwargs.get('Mark_WellKnownName')
    Label_PropertyName = kwargs.get('Label_PropertyName', 'label')
    Label_fill = kwargs.get('Label_fill')
    Label_fill_opacity = kwargs.get('Label_fill-opacity')
    Label_stroke = kwargs.get('Label_stroke')
    Label_stroke_witdth = kwargs.get('Label_stroke-witdth')
    Label_font_family = kwargs.get('Label_font-family')
    Label_font_size = kwargs.get('Label_font-size')
    Label_font_style = kwargs.get('Label_font-style')
    Label_font_weight = kwargs.get('Label_font-weight')
    Label_AnchorPointX = kwargs.get('Label_AnchorPointX')
    Label_AnchorPointY = kwargs.get('Label_AnchorPointY')
    Label_DisplacementX = kwargs.get('Label_DisplacementX')
    Label_DisplacementY = kwargs.get('Label_DisplacementY')
    Label_Rotation = kwargs.get('Label_Rotation')
    ExternalGraphic_href = kwargs.get('ExternalGraphic_href')
    ExternalGraphic_Format = kwargs.get('ExternalGraphic_Format')

    template = (
        '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        '<StyledLayerDescriptor version="1.0.0"\n'
            'xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"\n'
            'xmlns="http://www.opengis.net/sld"\n'
            'xmlns:ogc="http://www.opengis.net/ogc"\n'
            'xmlns:xlink="http://www.w3.org/1999/xlink"\n'
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
            '<NamedLayer>'
                '<UserStyle>'
                    '<FeatureTypeStyle>'
                        '<Rule>'
                            f'<Name>{Name}</Name>'
                            f'<Title>{Title}</Title>'
    )
    if MinScaleDenominator:
        template +=(        f'<MinScaleDenominator>{MinScaleDenominator}</MinScaleDenominator>')
    if MaxScaleDenominator:
        template +=(        f'<MaxScaleDenominator>{MaxScaleDenominator}</MaxScaleDenominator>')
    if Filter and Filter_PropertyName and Filter_Literal:
        template +=(
                            '<ogc:Filter>'
                                f'<ogc:{Filter}>'
                                    f'<ogc:PropertyName>{Filter_PropertyName}</ogc:PropertyName>'
                                    f'<ogc:Literal>{Filter_Literal}</ogc:Literal>'
                                f'</ogc:{Filter}>'
                            '</ogc:Filter>'
        )
    template +=(
                            '<PolygonSymbolizer>'
                                '<Graphic>'
    ) 
    if Mark_WellKnownName and not ExternalGraphic_href:
        template +=(
                                    '<Mark>'
                                        f'<WellKnownName>{Mark_WellKnownName}</WellKnownName>'
        )
        if Mark_fill or Mark_fill_opacity:
            template +=(                '<Fill>')
            if Mark_fill:
                template +=(                f'<CssParameter name="fill">{Mark_fill}</CssParameter>')
            if Mark_fill_opacity:
                template +=(                f'<CssParameter name="fill-opacity">{Mark_fill_opacity}</CssParameter>')
            template +=(                '</Fill>')
        if Mark_stroke or Mark_stroke_witdth:
            template +=(                '<Stroke>')
            if Mark_stroke:
                template +=(                f'<CssParameter name="stroke">{Mark_stroke}</CssParameter>')
            if Mark_stroke_witdth:
                template +=(                f'<CssParameter name="stroke-width">{Mark_stroke_witdth}</CssParameter>')
            template +=(                '</Stroke>')
        template +=(                '</Mark>')
    else:
        template +=(                '<ExternalGraphic>'
                                        f'<OnlineResource xlink:type="simple" xlink:href="{ExternalGraphic_href}" />'
                                        f'<Format>{ExternalGraphic_Format}</Format>'
                                    '</ExternalGraphic>'
        )
    if Size:
        template +=(                f'<Size>{Size}</Size>')
    if Opacity:
        template +=(                f'<Opacity>{Opacity}</Opacity>')
    if Rotation:
        template +=(                f'<Rotation>{Rotation}</Rotation>')
    template +=(
                                '</Graphic>'
                            '</PolygonSymbolizer>'
    )
    if Label_PropertyName:
        template +=(
                            '<TextSymbolizer>'
                                '<Label>'
                                    f'<ogc:PropertyName>{Label_PropertyName}</ogc:PropertyName>'
                                '</Label>'
        )
        #  '<Halo>'
        #  '    <Radius>3</Radius>'
        #  '    <Fill>'
        #  '        <CssParameter name="fill">#FFFFFF</CssParameter>'
        #  '    </Fill>'
        #  '</Halo>'
        if Label_font_family or Label_font_size or Label_font_style or Label_font_weight:
            template +=(        '<Font>')
            if Label_font_family:
                template +=(        f'<CssParameter name="font-family">{Label_font_family}</CssParameter>')
            if Label_font_size:
                template +=(        f'<CssParameter name="font-size">{Label_font_size}</CssParameter>')
            if Label_font_style:
                template +=(        f'<CssParameter name="font-style">{Label_font_style}</CssParameter>')
            if Label_font_weight:
                template +=(        f'<CssParameter name="font-weight">{Label_font_weight}</CssParameter>')
            template +=(        '</Font>')
        if Label_AnchorPointX or Label_AnchorPointY or Label_DisplacementX or Label_DisplacementY or Label_Rotation:
            template +=(
                                '<LabelPlacement>'
                                    '<PointPlacement>'
            )
            if Label_AnchorPointX or Label_AnchorPointY:
                template +=(
                                        '<AnchorPoint>'
                                            f'<AnchorPointX>{Label_AnchorPointX}</AnchorPointX>'
                                            f'<AnchorPointY>{Label_AnchorPointY}</AnchorPointY>'
                                        '</AnchorPoint>'
                )
            if Label_DisplacementX or Label_DisplacementY:
                template +=(
                                        '<Displacement>'
                                            f'<DisplacementX>{Label_DisplacementX}</DisplacementX>'
                                            f'<DisplacementY>{Label_DisplacementY}</DisplacementY>'
                                        '</Displacement>'
                )
            if Label_Rotation:
                template +=(            f'<Rotation>{Label_Rotation}</Rotation>')
            template +=(
                                    '</PointPlacement>'
                                '</LabelPlacement>'
            )
        if Label_fill or Label_fill_opacity:
            template +=(        '<Fill>')
            if Label_fill:
                template +=(        f'<CssParameter name="fill">{Label_fill}</CssParameter>')
            if Label_fill_opacity:
                template +=(        f'<CssParameter name="fill-opacity">{Label_fill_opacity}</CssParameter>')
            template +=(        '</Fill>')
        if Label_stroke or Label_stroke_witdth:
            template +=(        '<Stroke>')
            if Label_stroke:
                template +=(        f'<CssParameter name="stroke">{Label_stroke}</CssParameter>')
            if Label_stroke_witdth:
                template +=(        f'<CssParameter name="stroke-width">{Label_stroke_witdth}</CssParameter>')
            template +=(        '<Stroke>')
        # '<VendorOption name="autoWrap">60</VendorOption>'
        # '<VendorOption name="maxDisplacement">150</VendorOption>'
        template +=(        '<TextSymbolizer>')
    template +=(
                        '</Rule>'
                    '</FeatureTypeStyle>'
                '</UserStyle>'
            '</NamedLayer>'
        '</StyledLayerDescriptor>'
    )
    return template


# favorite_point_style = {
#     'Name': 'favorite_point_style',
#     'Title': 'favorite_point_style',
#     'Label_PropertyName': 'name',
#     'Label_fill': '#000000',
#     'Label_stroke': '#ffffff',
#     'Label_stroke-witdth': '2',
#     'Mark_WellKnownName': 'triangle',
#     'Mark_fill': '#ff0000',
#     'Mark_stroke': '#465232',
#     'Mark_stroke-width': '2'
#     # 'ExternalGraphic_href': '/static/my/icons/favorite-place.png',
#     # 'ExternalGraphic_Format': 'image/png',
# }


# favorite_region_style = {

# }

favorite_region_style = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
    xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
    xmlns="http://www.opengis.net/sld"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <NamedLayer>
    <Name>geometries_favoriteregion</Name>
    <UserStyle>
      <Name>geometries_favoriteregion</Name>
      <FeatureTypeStyle>
        <Rule>
          <Name>Single symbol</Name>
          <PolygonSymbolizer>
            <Fill>
              <CssParameter name="fill">#ffffff</CssParameter>
              <CssParameter name="fill-opacity">0.3</CssParameter>
            </Fill>
            <Stroke>
              <CssParameter name="stroke">#3399cc</CssParameter>
              <CssParameter name="stroke-width">2</CssParameter>
            </Stroke>
          </PolygonSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
'''


favorite_point_style = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<StyledLayerDescriptor version="1.0.0"
    xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
    xmlns="http://www.opengis.net/sld"
    xmlns:ogc="http://www.opengis.net/ogc"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <NamedLayer>
    <Name>geometries_favoritepoint</Name>
    <UserStyle>
      <Name>geometries_favoritepoint</Name>
      <FeatureTypeStyle>
        <Rule>
          <Name>Single symbol</Name>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>triangle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#db1e2a</CssParameter>
                </Fill>
              </Mark>
              <Size>14</Size>
              <Rotation>
                <ogc:Literal>180</ogc:Literal>
              </Rotation>
              <Displacement>
                <DisplacementX>0</DisplacementX>
                <DisplacementY>7</DisplacementY>
              </Displacement>
            </Graphic>
          </PointSymbolizer>
          <PointSymbolizer>
            <Graphic>
              <Mark>
                <WellKnownName>circle</WellKnownName>
                <Fill>
                  <CssParameter name="fill">#db1e2a</CssParameter>
                </Fill>
              </Mark>
              <Size>13</Size>
              <Displacement>
                <DisplacementX>0</DisplacementX>
                <DisplacementY>-3</DisplacementY>
              </Displacement>
            </Graphic>
          </PointSymbolizer>
        </Rule>
        <Rule>
          <TextSymbolizer>
            <Label>
              <ogc:PropertyName>name</ogc:PropertyName>
            </Label>
            <Font>
              <CssParameter name="font-size">13</CssParameter>
              <CssParameter name="font-weight">bold</CssParameter>
            </Font>
            <LabelPlacement>
              <PointPlacement>
                <AnchorPoint>
                  <AnchorPointX>0.5</AnchorPointX>
                  <AnchorPointY>0.5</AnchorPointY>
                </AnchorPoint>
                <Displacement>
                  <DisplacementX>0</DisplacementX>
                  <DisplacementY>18</DisplacementY>
                </Displacement>
              </PointPlacement>
            </LabelPlacement>
            <Halo>
              <Radius>3.5</Radius>
              <Fill>
                <CssParameter name="fill">#ffffff</CssParameter>
              </Fill>
            </Halo>
            <Fill>
              <CssParameter name="fill">#000000</CssParameter>
            </Fill>
            <VendorOption name="maxDisplacement">1</VendorOption>
          </TextSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>'''
