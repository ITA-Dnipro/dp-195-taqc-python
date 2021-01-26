from selenium.webdriver import Chrome

from base.base import Page, Success
from base.elements import RadioButton, RadioButtonGroup, Form, Block, InputField

# host = 'demo.opencart.com'


class Reason(RadioButtonGroup):

    contains = {
        'dead': {
            'locator': ('TAG_NAME', 'input'),
            'class': RadioButton
        },
        'faulty': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[2]/label/input'),
            'class': RadioButton
        },
        'error': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[3]/label/input'),
            'class': RadioButton
        },
        'other': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[4]/label/input'),
            'class': RadioButton
        },
        'wrong': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[5]/label/input'),
            'class': RadioButton
        }
    }


class ProductOpened(RadioButtonGroup):

    contains = {
        'yes': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[5]/div/label[1]/input'),
            'class': RadioButton
        },
        'no': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[5]/div/label[2]/input'),
            'class': RadioButton
        }
    }


class OrderInfo(Block):

    contains = {
        'first_name': {
            'locator': ('ID', 'input-firstname'),
            'class': InputField
        },
        'last_name': {
            'locator': ('ID', 'input-lastname'),
            'class': InputField
        },
        'email': {
            'locator': ('ID', 'input-email'),
            'class': InputField
        },
        'telephone': {
            'locator': ('ID', 'input-telephone'),
            'class': InputField
        },
        'order_id': {
            'locator': ('ID', 'input-order-id'),
            'class': InputField
        },
        'order_date': {
            'locator': ('ID', 'input-date-ordered'),
            'class': InputField
        },
    }


class ProductInfo(Block):

    contains = {
        'name': {
            'locator': ('ID', 'input-product'),
            'class': InputField
        },
        'code': {
            'locator': ('ID', 'input-model'),
            'class': InputField
        },
        'quantity': {
            'locator': ('ID', 'input-quantity'),
            'class': InputField
        },
        'reason': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[4]'),
            'class': Reason
        },
        'is_opened': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]/div[5]'),
            'class': ProductOpened
        },
        'details': {
            'locator': ('ID', 'input-comment'),
            'class': InputField
        },
    }


class ReturnForm(Form):

    contains = {
        'personal': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[1]'),
            'class': OrderInfo
        },
        'product': {
            'locator': ('XPATH', '//*[@id="content"]/form/fieldset[2]'),
            'class': ProductInfo
        },
    }

    def fill_out(self, **kwargs):

        self.personal.first_name.fill(kwargs.get('first_name'))
        self.personal.last_name.fill(kwargs.get('last_name'))
        self.personal.email.fill(kwargs.get('email'))
        self.personal.telephone.fill(kwargs.get('telephone'))
        self.personal.order_id.fill(kwargs.get('order_id'))
        self.product.name.fill(kwargs.get('product_name'))
        self.product.code.fill(kwargs.get('product_code'))
        self.product.quantity.fill(kwargs.get('quantity'))
        self.product.reason.select_option(kwargs.get('reason'))
        self.product.is_opened.select_option(kwargs.get('is_opened'))
        self.product.details.fill(kwargs.get('details'))


class ReturnPage(Page):

    url = 'index.php?route=account/return/add'

    contains = {
        'form': {
            'locator': ('CLASS_NAME', 'form-horizontal'),
            'class': ReturnForm
        },
    }


# if __name__ == "__main__":
#     page = ReturnPage()
#     page.load(host)
#     page.form.fill_out(
#         first_name='John',
#         last_name='Doe',
#         email='kek@gmail.com',
#         telephone='2212211',
#         order_id='5',
#         product_name='iphone',
#         product_code='i5',
#         reason='wrong',
#         is_opened='yes',
#         details='asdsdsadasdsddwwscscew'
#     )
#     page.form.submit()
#     # print(page.get_alerts())
#     assert Success().is_available
