example:
{% if grains['os_family'] == 'RedHat' %}
  package: vim-enhanced
{% else %}
  package: vim
{% endif %}
