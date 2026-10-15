from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import ToolCall


dataset = EvaluationDataset(
    goldens=[
        Golden(
            input="I am user130. Please refund my headphones.",
            expected_output="A refund ticket for $35 has been issued successfully.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date"),
            ],
        ),

        Golden(
            input="I am user123. Please refund my book.",
            expected_output="No refund will be issued because the book was purchased more than 30 days ago.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="get_today_date")
            ],
        ),

        Golden(
            input="I am user131. Please refund only my mouse.",
            expected_output="A refund ticket for $20 has been issued for the mouse only.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ],
        ),

        Golden(
            input="I am user132. Refund my paintbrush and canvas.",
            expected_output="A refund ticket for $34 has been issued for the paintbrush and canvas.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ],
        ),

        Golden(
            input="I am user129. How much would I get for returning my usb_drive? Do not issue a refund ticket.",
            expected_output="You would receive $16 for the USB drive. No refund ticket has been issued.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="get_today_date")
            ],
        ),

        Golden(
            input="I would like to request a refund.",
            expected_output="Could you please provide your username?",
            expected_tools=[],
        ),

        Golden(
            input="I am user999. I want to refund my book.",
            expected_output="No customer account was found for user999. No refund ticket has been issued.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
            ],
        ),

        Golden(
            input="I am user131. Please refund my keyboard.",
            expected_output="The keyboard was not found in your purchase history. No refund ticket has been issued.",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
            ],
        ),
    ]
)