from typing import List, Optional

from pydantic import BaseModel


class PickUpStoreInfo(BaseModel):
    pick_up_store_address: str
    pick_up_store_name: str
    pick_up_store_open_hour: List[str]
    pick_up_store_code: str


class OrderItem(BaseModel):
    tax_amount: str
    pick_up_store_info: PickUpStoreInfo
    reason: str
    sla_time_stamp: str
    purchase_order_id: str
    voucher_seller: str
    payment_time: str
    voucher_code_seller: str
    voucher_code: str
    package_id: str
    buyer_id: str
    variation: str
    voucher_code_platform: str
    purchase_order_number: str
    show_gift_wrapping_tag: str
    sku: str
    gift_wrapping: str
    order_type: str
    show_personalization_tag: str
    invoice_number: str
    cancel_return_initiator: str
    shop_sku: str
    is_reroute: str
    stage_pay_status: str
    sku_id: str
    tracking_code_pre: str
    order_item_id: str
    shop_id: str
    order_flag: str
    is_fbl: str
    name: str
    delivery_option_sof: str
    fulfillment_sla: str
    order_id: str
    status: str
    paid_price: str
    product_main_image: str
    voucher_platform: str
    product_detail_url: str
    warehouse_code: str
    promised_shipping_time: str
    shipping_type: str
    created_at: str
    voucher_seller_lpi: str
    shipping_fee_discount_platform: str
    personalization: str
    wallet_credits: str
    updated_at: str
    currency: str
    shipping_provider_type: str
    shipping_fee_original: str
    voucher_platform_lpi: str
    is_digital: str
    item_price: str
    shipping_service_cost: str
    tracking_code: str
    shipping_fee_discount_seller: str
    reason_detail: str
    shipping_amount: str
    return_status: str
    priority_fulfillment_tag: str
    shipment_provider: str
    voucher_amount: str
    extra_attributes: str
    digital_delivery_info: str


class Data(BaseModel):
    order_number: str
    order_id: str
    order_items: List[OrderItem]


class ResponseMultipleOrderItems(BaseModel):
    code: str
    data: Optional[List[Data]]
    request_id: str
