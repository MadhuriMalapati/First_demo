
# homepage_heading_css = 'h1.heading'
# homepage_heading_xpath = '//h1[@class="heading"]'
#https://the-internet.herokuapp.com/abtest

hp_link_ab_testing_xpath = '//a[text()="A/B Testing"]'
hp_ab_testing_xpath_desc = "//h3[text()='A/B Test Variation 1']"
hp_ab_testing_paragraph="//p[contains(text(),'split')]"
hp_footer_section="//a[text()='Elemental Selenium']"
hp_other_way_of_footer_section="//div[text()='Powered by ']/a"
hp_parent_value_of_footer="//a[text()='Elemental Selenium']/parent::div"


#https://the-internet.herokuapp.com/add_remove_elements/

hp_link_add_remove_Xpath = '//a[text()="Add/Remove Elements"]'
hp_add_remove_desc="//h3[text()='Add/Remove Elements']"
hp_Add_element_path="//button[text()='Add Element']"
hp_Delete_button_path="//button[text()='Delete']"
hp_Delete_button_path_through_index="//button[text()='Delete'][2]"
hp_parent_select="//button[text()='Delete']/parent::div"
hp_ancestor_element="//a[text()='Add/Remove Elements']/ancestor::li"

#https://the-internet.herokuapp.com/basic_auth
hp_Basic_Auth_Xpath="//a[text()='Basic Auth']"
hp_Basic_Auth_Xpath_parent="//a[text()='Basic Auth']/parent::li"
hp_basic_auth_xpath_preceding="//a[text()='Basic Auth']/preceding::li"
hp_basic_auth_xpath_following="//a[text()='Basic Auth']/following::li"

#https://the-internet.herokuapp.com/broken_images
hp_broken_images_xpath="//a[text()='Broken Images']"
hp_broken_images_desc="//h3[text()='Broken Images']"
hp_parent="//a[text()='Broken Images']/parent::li"
hp_ancestor_values="//a[text()='Broken Images']/ancestor::li"
hp_position_value="(//div)[position()=6]"
hp_last="(//div)[last()]"

















