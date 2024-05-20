from typing import Dict, List, Optional

from pydantic import BaseModel


class AddressBilling(BaseModel):
    country: str
    address3: str
    phone: str
    address2: str
    city: str
    address1: str
    post_code: str
    phone2: str
    last_name: str
    address5: str
    address4: str
    first_name: str


class AddressShipping(BaseModel):
    country: str
    address3: str
    phone: str
    address2: str
    city: str
    address1: str
    post_code: str
    phone2: str
    last_name: str
    address5: str
    address4: str
    first_name: str


class Order(BaseModel):
    voucher_platform: str
    voucher: str
    warehouse_code: str
    order_number: str
    voucher_seller: str
    created_at: str
    voucher_code: str
    gift_option: str
    shipping_fee_discount_platform: str
    customer_last_name: str
    promised_shipping_times: str
    updated_at: str
    price: str
    national_registration_number: str
    shipping_fee_original: str
    payment_method: str
    address_updated_at: str
    buyer_note: str
    customer_first_name: str
    shipping_fee_discount_seller: str
    shipping_fee: str
    branch_number: str
    tax_code: str
    items_count: str
    delivery_info: str
    statuses: List
    address_billing: AddressBilling
    extra_attributes: str
    order_id: str
    remarks: str
    gift_message: str
    address_shipping: AddressShipping


class Data(BaseModel):
    count: str
    countTotal: str
    orders: List[Order]


class ResponseOrders(BaseModel):
    code: str
    data: Optional[Data]
    request_id: str
