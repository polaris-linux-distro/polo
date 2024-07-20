# Function to get value from an INI file
function get_ini_value() {
  local section=$1
  local key=$2
  local file=$3

  awk -F '=' -v section="$section" -v key="$key" '
    $0 ~ "\\[" section "\\]" { in_section=1; next }
    $0 ~ "^\\[" { in_section=0 }
    in_section && $1 == key { print $2; exit }
  ' "$file"
}