# 4. CONFIGURE CYCLONEDDS
cat << 'EOF' > ~/.ros/cyclonedds_config.xml
<CycloneDDS>
  <Domain>
    <General>
      <NetworkInterfaceAddress>wlo1</NetworkInterfaceAddress>
    </General>
  </Domain>
</CycloneDDS>
EOF
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=file://$HOME/.ros/cyclonedds_config.xml
